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



cut from product_list page from line 23

     <div class="d-flex mb-1">
                  <div class="form-check form-option form-check-justified mb-2">
                     <input class="form-check-input" type="radio" name="size1" id="s1" checked>
                     <label class="form-option-label" style="font-size: 0.9375rem !important" for="s1">Small</label>
                  </div>
                  <div class="form-check form-option form-check-justified mb-2">
                     <input class="form-check-input" type="radio" name="size1" id="m1">
                     <label class="form-option-label" style="font-size: 0.9375rem !important" for="m1">Medium</label>
                  </div>
                  <div class="form-check form-option form-check-justified mb-2">
                     <input class="form-check-input" type="radio" name="size1" id="l1">
                     <label class="form-option-label" style="font-size: 0.9375rem !important" for="l1">Large</label>
                  </div>
               </div>
               <div class="d-flex mb-3">
                  <div class="form-check form-option form-check-justified mb-2">
                     <input class="form-check-input" type="radio" name="base1" id="thin1" chekced>
                     <label class="form-option-label"  style="font-size: 0.9375rem !important" for="thin1">Thin</label>
                  </div>
                  <div class="form-check form-option form-check-justified mb-2">
                     <input class="form-check-input" type="radio" name="base1" id="standard1" checked="">
                     <label class="form-option-label" style="font-size: 0.9375rem !important" for="standard1">Standard</label>
                  </div>


