import pdftables_api

c = pdftables_api.Client('r2swekply0w9')
c.xlsx('nombredelarchivo.pdf', 'nombredesalida') 
#replace c.xlsx with c.csv to convert to CSV
#replace c.xlsx with c.xml to convert to XML
#replace c.xlsx with c.html to convert to HTML