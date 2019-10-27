{% extends"base.html" %}

{%  blocktitle %}Bensínstöðvar {% endblock %}
{% block content %}

<table>
    <caption>allar bensínstöðvar fyrirtækisins</caption>
    <tr>
        <th>Fyrirtæki</th><th>staður</th>
    </tr>

    {% set cnt = [] %}
    {% for item in gogn['results'] %}
    <tr>
        {% if item.company == com %}
        {% do cnt.append(item.comapny) %}
        <td><a href = "/moreinfo/{{item.key}}">{{item.comapny}}</a></td>
        <td>{{ item.name }}</td>
        {%  endif %}
    </tr>
    {% endfor %}
</table>
<h3>Fjöldi stöðva: {{ cnt | length }}</h3>