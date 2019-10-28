{% extends "base.html" %}
{%  block title %}Eldsneytisverð - miðannarverkefni - json{% endblock %}
{% block content %}
<div class="wrapper">
    {%  set comCo = [] %}
    {% for item in gogn["results"] %}
        {% if item.company not in comCo %}
            {% do Co.append(item.company) %}
            <div class="box">
                <a href="/company/{{ item.company }}">
                    <img src="static/{{ item.company }}.png" title="{{ item.company }}">
                </a>
            </div>
        {% endif %}
    {% endfor %}
</div>
<div class="kort">
</div>

<p> Fyrirtækin birtast aðeins einu sinni á forsíðu</p>
{% endblock %}