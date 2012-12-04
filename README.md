# mezzanine-slides

Add simple slide functionality to your Mezzanine based website allowing for
beautiful banners at the tops of pages.


# Setup

Add `mezzanine_slides` to your `INSTALLED_APPS` and syncdb. Migrations are
included if you use South. You can use the templates included by running
`collecttemplates` but this will overwrite any changes you have made to your
`base.html` and `pages/page.html` templates. If you wish to add the template
markup yourself see Templates below.


# Templates

Add this to your `pages/page.html` anywhere as long as it's not inside another
block:

    {% block slides %}{% if page.slide_set.all %}
    <div class="row">
    <div class="span12">
        <ul class="rslides">{% for image in page.slide_set.all %}
            <li><img src="{{ image.file.url }}" alt="{{ image.description }}"/></li>
        {% endfor %}</ul>
    </div>
    </div>
    {% endif %}{% endblock %}

Add this to `base.html` where you would like the slides to appear, which is
usually between your main content and the navigation:

    {% block slides %}{% endblock %}

Notice that I include the `row` and `span12` classes on the `pages/page.html`
template so that if you don't have any slides then nothing is added to the page.

Now you'll need to include the CSS and JS in your compress areas of your
`base.html` template:

    {% compress css %}
    ...
    <link rel="stylesheet" href="{{ STATIC_URL }}css/responsiveslides.css">
    {% endcompress %}

    
    {% compress js %}
    ...
    <script src="{{ STATIC_URL }}js/responsiveslides.min.js"></script>
    {% endcompress %}

Lastly you'll need to invoke the slides JavaScript by putting
`$('.rslides').responsiveSlides();` on in your JavaScript somewhere. In the
`base.html` template I put this in the header around line 34 where I found some
other JavaScript functions to just make it easy and try to conform to the
original Mezzanine as much as possible, here is an excerpt of the area:

    <script>
    $(function() {
        ...
        $('.rslides').responsiveSlides();
    });
    </script>

## License (Simplified BSD)

Copyright (c) Isaac Bythewood  
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice,
   this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
