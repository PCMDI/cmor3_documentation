module cmip7_fortran_common
  use cmor_users_functions
  implicit none

  integer, parameter :: nlon = 4
  integer, parameter :: nlat = 3
  integer, parameter :: ntimes = 2
  real, parameter :: missing_value = 1.0e20

contains

  subroutine get_example_args(tables_path, input_path, output_dir)
    character(len=*), intent(out) :: tables_path
    character(len=*), intent(out) :: input_path
    character(len=*), intent(out) :: output_dir

    call get_command_argument(1, tables_path)
    call get_command_argument(2, input_path)
    call get_command_argument(3, output_dir)

    if (len_trim(tables_path) == 0) tables_path = "./cmip7-cmor-tables/tables"
    if (len_trim(input_path) == 0) input_path = "./CMIP7_input_example.json"
    if (len_trim(output_dir) == 0) output_dir = "output"
  end subroutine get_example_args

  subroutine load_shared_user_input(input_path, output_dir, frequency)
    character(len=*), intent(in) :: input_path
    character(len=*), intent(in) :: output_dir
    character(len=*), intent(in), optional :: frequency
    integer :: ierr

    ierr = cmor_dataset_json(trim(input_path))
    call check_status("cmor_dataset_json", ierr)

    ierr = cmor_set_cur_dataset_attribute("outpath", trim(output_dir), 1)
    call check_status("cmor_set_cur_dataset_attribute(outpath)", ierr)

    if (present(frequency)) then
      ierr = cmor_set_cur_dataset_attribute("frequency", trim(frequency), 1)
      call check_status("cmor_set_cur_dataset_attribute(frequency)", ierr)
    endif
  end subroutine load_shared_user_input

  subroutine check_status(call_name, ierr)
    character(len=*), intent(in) :: call_name
    integer, intent(in) :: ierr

    if (ierr /= 0) then
      write(*, '(a, i0)') trim(call_name)//" failed with status ", ierr
      stop 1
    endif
  end subroutine check_status

  subroutine check_id(call_name, cmor_id)
    character(len=*), intent(in) :: call_name
    integer, intent(in) :: cmor_id

    if (cmor_id < 0) then
      write(*, '(a, i0)') trim(call_name)//" failed with id ", cmor_id
      stop 1
    endif
  end subroutine check_id

  subroutine check_grid_id(call_name, cmor_id)
    character(len=*), intent(in) :: call_name
    integer, intent(in) :: cmor_id

    if (cmor_id > -CMOR_MAX_GRIDS) then
      write(*, '(a, i0)') trim(call_name)//" failed with grid id ", cmor_id
      stop 1
    endif
  end subroutine check_grid_id

  subroutine apply_cmip7_variable_metadata(var_id, tables_path, realm, &
       table_entry, frequency, region)
    integer, intent(in) :: var_id
    character(len=*), intent(in) :: tables_path
    character(len=*), intent(in) :: realm
    character(len=*), intent(in) :: table_entry
    character(len=*), intent(in) :: frequency
    character(len=*), intent(in) :: region
    character(len=2048) :: compound_name
    character(len=2048) :: cell_measures
    character(len=2048) :: long_name
    integer :: ierr
    logical :: found

    call cmip7_compound_name(realm, table_entry, frequency, region, &
         compound_name)

    cell_measures = ""
    call lookup_json_string(trim(tables_path)//"/CMIP7_cell_measures.json", &
         trim(compound_name), cell_measures, found)
    ierr = cmor_set_variable_attribute(var_id, "cell_measures", &
         trim(cell_measures))
    call check_status("cmor_set_variable_attribute(cell_measures)", ierr)

    long_name = ""
    call lookup_json_string(trim(tables_path)//"/CMIP7_long_name_overrides.json", &
         trim(compound_name), long_name, found)
    if (found) then
      ierr = cmor_set_variable_attribute(var_id, "long_name", trim(long_name))
      call check_status("cmor_set_variable_attribute(long_name)", ierr)
    endif
  end subroutine apply_cmip7_variable_metadata

  subroutine cmip7_compound_name(realm, table_entry, frequency, region, &
       compound_name)
    character(len=*), intent(in) :: realm
    character(len=*), intent(in) :: table_entry
    character(len=*), intent(in) :: frequency
    character(len=*), intent(in) :: region
    character(len=*), intent(out) :: compound_name
    character(len=1024) :: normalized_entry
    integer :: i

    normalized_entry = table_entry
    do i = 1, len_trim(normalized_entry)
      if (normalized_entry(i:i) == "_") normalized_entry(i:i) = "."
    enddo

    compound_name = trim(realm)//"."//trim(normalized_entry)//"."// &
         trim(frequency)//"."//trim(region)
  end subroutine cmip7_compound_name

  subroutine lookup_json_string(path, key, value, found)
    character(len=*), intent(in) :: path
    character(len=*), intent(in) :: key
    character(len=*), intent(out) :: value
    logical, intent(out) :: found
    character(len=8192) :: line
    character(len=2050) :: search_key
    integer :: colon_pos
    integer :: ierr
    integer :: quote_1
    integer :: quote_2
    integer :: start_pos
    integer :: unit

    value = ""
    found = .false.
    search_key = '"'//trim(key)//'"'

    open(newunit=unit, file=trim(path), status="old", action="read", &
         iostat=ierr)
    if (ierr /= 0) then
      write(*, '(a)') "Could not open CMIP7 metadata table: "//trim(path)
      stop 1
    endif

    do
      read(unit, '(a)', iostat=ierr) line
      if (ierr /= 0) exit
      if (index(line, trim(search_key)) == 0) cycle

      colon_pos = index(line, ":")
      if (colon_pos == 0) exit

      quote_1 = index(line(colon_pos + 1:), '"')
      if (quote_1 == 0) exit

      start_pos = colon_pos + quote_1
      quote_2 = index(line(start_pos + 1:), '"')
      if (quote_2 == 0) exit

      value = line(start_pos + 1:start_pos + quote_2 - 1)
      found = .true.
      exit
    enddo

    close(unit)
  end subroutine lookup_json_string

end module cmip7_fortran_common
