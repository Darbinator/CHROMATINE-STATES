#!/usr/bin/env python

import os
import sys
from yattag import Doc
from name import name
from coordinates import coordinates
from state_to_gene import state_to_gene
from state_to_name import state_to_name
from results import results
from decimal import *


###

dirname = os.path.dirname
CSE_PATH = dirname(dirname(os.path.realpath(__file__)))

##


doc, tag, text = Doc().tagtext()

doc.asis('<!DOCTYPE html>')

with tag('html'):

	with tag('head'):

		doc.stag('meta', charset="utf-8")

		doc.stag('link',rel='stylesheet', href='style.css')

		with tag('title'):

			text(name)

		doc.stag('link', rel='stylesheet', type='text/css', href=CSE_PATH+"/javascript/DataTables/datatables.css")
		
		doc.asis("<script type='text/javascript' charset='utf-8' src ='"+CSE_PATH+"/javascript/DataTables/datatables.js'></script>")

		with tag('script'):

			text(''' 
					$(document).ready( function () {
   						$('#main_results').DataTable( {
   						"order": [[ 3, "desc" ]]

   						} );

						} );''')
		



	with tag('body'):

		with tag('header'):

			with tag('h1'):

				text("Results")



		with tag("nav"):

			with tag("div"):


				with tag("ul"):

					with tag("li",):

						with tag("a", klass='nav', rel="external", href="index.html"):

							text("Main results")

						with tag("a", klass='nav', rel="external", href="genes.html"):

							text("Genes")

						with tag("a", klass='nav', rel="external", href="help.html"):

							text("Help")









		doc.asis('<br> <br> <br>')

		with tag('section', klass='table'):

			with tag('table', id='main_results'):

				with tag('thead'):

					with tag('tr'):

						header = ("State","Pvalue ajustée","Oddsratio",
							"Nombre de gènes total (background)","Nombre de gènes total ciblés  ",
							"Nombre de gènes entrés","Nombre de gènes entrés ciblés","Description","Sens","Pvalue ajustée (random sampling) ")

						for head in header:

							with tag('td',klass='head'):

								text(head)






				with tag('tbody'):



					for state, infos in sorted(results.items(), key=lambda kv: (kv[1][7],kv[1][0])):

						with tag('tr'):

							with tag('td'):

								with tag('a',klass='states', rel="external", href='states_'+str(state)+'.html'):

									text(state)




							for i in range(len(infos)):

									if i == 5:

										with tag('td'):

											with tag('a', rel='external', href='state_to_genes'+str(state)+'.html',title = 'To see the genes associated with the state'):

												text(infos[i])

									elif infos[7] == 'over':

										with tag('td', klass='over'):

												text(infos[i])

									else:

										with tag('td', klass='under'):

											text(infos[i])

		doc.stag('img',src=CSE_PATH+"/images/matrix.png",klass='matrix')

		doc.asis("<script type='text/javascript' src='"+CSE_PATH+"/javascript/show_state_to_genes.js'></script>")





result = doc.getvalue()

with open(CSE_PATH+"/html/index.html", "w") as file:
    file.write(result)