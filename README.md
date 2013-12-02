# django_mce_spellcheck

## Description

[Django](http://www.djangoproject.com) app that provides a backend for the  [tinymce](http://www.tinymce.com/) spellecheck plugin that allows you to spellcheck your documents. It is configured to work by default with a [Mezzanine](https://github.com/stephenmcd/mezzanine) installation. Spell checking on the backend is provided by [enchant](http://pythonhosted.org/pyenchant/). 

## Screenshots

The spellchecker in action:

![The spellchecker in action](https://raw.github.com/seanodonnell/django_mce_spellcheck/master/screenshots/django_mce_spellcheck.png)

## Requirements

[enchant](http://pythonhosted.org/pyenchant/)

If you wish to spellcheck a language other than english, you may need to install additional dictionaries. Check the enchant documentation for details.

## INSTALLATION

Place the app on your python path

Add django_mce_spellcheck to your ```INSTALLED APPS```

Find your tinymce_setup.js file and add spellchecker to the plugins line, here is an example:

    plugins: "inlinepopups,contextmenu,tabfocus,searchreplace,fullscreen,advimage,advlink,paste,media,table,spellchecker"

Also add it to your theme, here is another example:

    theme_advanced_buttons1: "bold,italic,|,link,unlink,|,image,|,media,charmap,|,code,|,table,|,bullist,numlist,blockquote,|,undo,redo,|,formatselect,|,search,replace,|,spellchecker,|,fullscreen,",

Finally add the spellchecker view address, if you are using the suggested urls.py entry below, this should be:

    spellchecker_rpc_url : '/spellcheck/',

The spellchecker plugin can cause some forms to malfunction when the spellcheck is active. In order to fix this, I have created a small snippet, which automatically turns off the spellcheck plugin in all active tinymce instances on the page, whenever a submit button is clicked. This script assumes that jquery is available. I put this code at the bottom of my tinymce_setup.js file. 

This snippet can be downloaded from  https://raw.github.com/seanodonnell/django_mce_spellcheck/master/django_mce_spellcheck/static/js/spellcheck_fix.js, but here is the source

    $(document).ready(function(){
    $('input[type="submit"]').click(function(){
            if (typeof window.tinyMCE !== 'undefined') {
                for (var id in tinyMCE.editors) {
                    var ed = tinyMCE.editors[id];
                    if (ed.plugins && ed.plugins.spellchecker && ed.plugins.spellchecker.active) {
                        ed.plugins.spellchecker._done();
                    }
                }
            }
    });
    });

Include the apps  urls to your urls.py. In a mezzanine installation, make sure this is before the mezzanine.urls include, as this includes a catchall. Example:

    ("^spellcheck/", include("django_mce_spellcheck.urls")),
    ("^", include("mezzanine.urls")),

## Configuration 

The app includes a copy of the spellcheck plugin from https://github.com/aljosa/django-tinymce/. If you are using staticfiles, this may become the active version of the plugin. It contains several small tweaks to the stock plugin, but if you would rather use the tinymce version, remove
 
/static/grapelli/tinymce/jscripts/tiny_mce/plugins/spellchecker

## AUTHORS

[seanodonnell](https://github.com/seanodonnell/)
backend code based on based on https://github.com/aljosa/django-tinymce/blob/master/tinymce/views.py

