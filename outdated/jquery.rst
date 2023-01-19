:github_url: https://github.com/sjfke/nonbleedingedge/blob/master/outdated/jquery.rst

*****************
jQuery CheatSheet
*****************

.. important:: Very early incomplete draft please ignore

Selectors
=========
::

	$("div") - all <div> tags
	$("#surname") - element id="surname"
	$(".warning") - element class="warning"

jQuery Object (array like)::
	
	$("body").length - there is only 1 body
	$("body")[0] - <body>..</body>

	$("body").size() - object-like equivalent of length
	$("body").get(0) - <body>..</body>
	
	$("body").jquery - 2.2.4 exists is a jQuery object
	$("body").selector - "body"
	$("body").context "#document"
	
	$(".tab").length // 12 tab elements 
