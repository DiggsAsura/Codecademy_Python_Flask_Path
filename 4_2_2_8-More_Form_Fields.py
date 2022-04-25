# 4. Introduction to Flask
# 2. Jinja2 Templates and Forms
# 2. Flask Forms
# 8. More Form Fields

'''
We've now covered the operation cycle of forms using FlaskWTF. Now let's look at
some additional form fields included in WTForms.

- TextArea Field -
The TextAreaField is a text field that supports multi-line input. The data
returned from a TextAreaField instance is a string that may include more
whitespace characters such as newlines or tabs.

### Form class declaration
my_text_area = TextAreaField("Text Area Label")

- BooleanField -
A checkbox element is created using the BooleanField object. The data returned
from a BooleanField instance is either True or False.

### Form class declaration
my_checkbox = BooleanField("Checkbox Label")

- RadioField -
A radio button group is created using the RadioField object. Since there are 
multiple buttons in this group, the instance declaration takes an argument
for the group lavel and a keyword argument choices which takes a list of tuples.

Each tuple represents a button in the group and contains the button identifier
string and the button label string

### Form class declaration
my_radio_group = RadioField("Radio Group Label", 
  choices=[
    ("id1", "RadioButton1"),
    ("id2", "RadioButton2"),
    ("id3", "RadioButton3")])

Since the RadioField() instance generally contains multiple buttons it is necessary
to iterate through it to access the components of the subfields.

'''

# This starting to get more fun! Using forms is valuable.

# A common practice when creating forms with Flask is to define the forms in
# a separate file and import them into the main app.

# see 4_2_2_8-forms.py, 4_2_2_8-app.py and 4_2_2_8-index.html


