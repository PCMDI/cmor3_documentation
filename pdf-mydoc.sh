echo 'Killing all Jekyll instances'
kill -9 $(ps aux | grep '[j]ekyll' | awk '{print $2}')
clear

echo "Building PDF-friendly HTML site for Mydoc ...";
bundle exec jekyll serve --detach --config _config.yml,pdfconfigs/config_mydoc_pdf.yml;
echo "done";

echo "Building the PDF ...";
prince --javascript --input-list=_site/doc_pdf/pdfconfigs/prince-list.txt -o pdf/mydoc.pdf;
echo "done";

echo 'Kill Jekyll instance'
kill -9 $(ps aux | grep '[j]ekyll' | awk '{print $2}')
clear
