Django foundation filefield widget
===================================

This module provides a form widget to style file inputs in a foundation fashion.


Installation
------------

Install with pip::

    pip install django-foundation-filefield-widget


Add `foundation_filefield_widget` app to your `INSTALLED_APPS`

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'foundation_filefield_widget',
    )

Use the widget in your forms :

.. code-block:: python

    from django import forms
    from foundation_filefield_widget.widgets import FoundationFileInput, FoundationImageInput

    class MyForm(forms.Form):
        my_file = forms.FileField(widget=FoundationFileInput)
        my_image = forms.FileField(widget=FoundationImageInput)


Don't forget to include the media part of your form in your templates.

If you want to easily define forms you should look into `crispy-forms <http://django-crispy-forms.readthedocs.org>`_
And if you want to define forms styled with Foundation you should also check `crispy-forms-foundation <http://crispy-forms-foundation.readthedocs.org>`_
