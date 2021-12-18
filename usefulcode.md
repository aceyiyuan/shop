form validation-allauth 

   {% for key, value in form.errors.items %}
   <li>{% if key != '__all__' %}{{ key }} {% endif %}{{ value }}</li>
   {% endfor %}

https://stackoverflow.com/questions/39183479/django-all-auth-form-errors-not-displaying
{% if form.errors %}
{% for field in form %}
    {% for error in field.errors %}
        <div class="alert alert-error">
            <strong>{{ error|escape }}</strong>
        </div>
    {% endfor %}
{% endfor %}
{% for error in form.non_field_errors %}
    <div class="alert alert-error">
        <strong>{{ error|escape }}</strong>
    </div>
{% endfor %}
{% endif %}



#2b3445 


base html line 65


    {% if messages %}
    <div>
      <strong>Messages:</strong>
      <ul>
        {% for message in messages %}
        <li>{{message}}</li>
        {% endfor %}
      </ul>
    </div>
    {% endif %}




