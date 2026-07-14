#include "cmip7_c_common.h"

#include <json-c/json.h>
#include <string.h>

static void copy_string(char *out, size_t out_size, const char *value) {
  if (out_size > 0) {
    snprintf(out, out_size, "%s", value);
  }
}

static void join_path(char *out, size_t out_size, const char *left,
                      const char *right) {
  size_t left_len = strlen(left);

  if (left_len > 0 && left[left_len - 1] == '/') {
    snprintf(out, out_size, "%s%s", left, right);
  } else {
    snprintf(out, out_size, "%s/%s", left, right);
  }
}

static void compound_name(char *out, size_t out_size, const char *realm,
                          const char *table_entry, const char *frequency,
                          const char *region) {
  char normalized[CMOR_MAX_STRING];
  size_t i;

  copy_string(normalized, sizeof(normalized), table_entry);
  for (i = 0; normalized[i] != '\0'; ++i) {
    if (normalized[i] == '_') {
      normalized[i] = '.';
    }
  }
  snprintf(out, out_size, "%s.%s.%s.%s", realm, normalized, frequency, region);
}

static void check_status(const char *call_name, int status) {
  if (status != 0) {
    fprintf(stderr, "%s failed with status %d\n", call_name, status);
    exit(1);
  }
}

void cmip7_get_example_args(int argc, char **argv, const char **tables_path,
                            const char **input_path, const char **output_dir) {
  *tables_path = argc > 1 && argv[1][0] != '\0' ? argv[1]
                                                 : "./cmip7-cmor-tables/tables";
  *input_path = argc > 2 && argv[2][0] != '\0' ? argv[2]
                                               : "./CMIP7_input_example.json";
  *output_dir = argc > 3 && argv[3][0] != '\0' ? argv[3] : "output";
}

void cmip7_load_shared_user_input(const char *input_path,
                                  const char *output_dir,
                                  const char *frequency) {
  check_status("cmor_dataset_json", cmor_dataset_json((char *)input_path));
  check_status("cmor_set_cur_dataset_attribute(outpath)",
               cmor_set_cur_dataset_attribute("outpath", (char *)output_dir,
                                              1));
  if (frequency != NULL) {
    check_status("cmor_set_cur_dataset_attribute(frequency)",
                 cmor_set_cur_dataset_attribute("frequency", (char *)frequency,
                                                1));
  }
}

static int lookup_json_string(const char *path, const char *root_name,
                              const char *key, char *value, size_t value_size) {
  json_object *document = json_object_from_file(path);
  json_object *root = NULL;
  json_object *entry = NULL;

  value[0] = '\0';
  if (document == NULL) {
    fprintf(stderr, "Could not open CMIP7 metadata table %s\n", path);
    exit(1);
  }

  if (json_object_object_get_ex(document, root_name, &root) &&
      json_object_object_get_ex(root, key, &entry)) {
    copy_string(value, value_size, json_object_get_string(entry));
    json_object_put(document);
    return 1;
  }

  json_object_put(document);
  return 0;
}

void cmip7_get_cell_measures(const char *tables_path, const char *realm,
                             const char *table_entry, const char *frequency,
                             const char *region, char *value,
                             size_t value_size) {
  char key[CMOR_MAX_STRING];
  char path[CMIP7_PATH_MAX];

  compound_name(key, sizeof(key), realm, table_entry, frequency, region);
  join_path(path, sizeof(path), tables_path, "CMIP7_cell_measures.json");
  lookup_json_string(path, "cell_measures", key, value, value_size);
}

int cmip7_get_long_name_override(const char *tables_path, const char *realm,
                                 const char *table_entry, const char *frequency,
                                 const char *region, char *value,
                                 size_t value_size) {
  char key[CMOR_MAX_STRING];
  char path[CMIP7_PATH_MAX];

  compound_name(key, sizeof(key), realm, table_entry, frequency, region);
  join_path(path, sizeof(path), tables_path, "CMIP7_long_name_overrides.json");
  return lookup_json_string(path, "long_name_overrides", key, value,
                            value_size);
}
