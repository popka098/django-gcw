#!/bin/bash

files="main/views.py main/views_api.py main/models.py main/forms.py training/views.py training/models.py"

# run pylint
pylint --load-plugins=pylint_django --disable="C0114, C0115, C0116" $files | tee pylint.txt

# get badge
mkdir public
score=$(sed -n 's/^Your code has been rated at \([-0-9.]*\)\/.*/\1/p' pylint.txt)
anybadge --value=$score --file=public/pylint.svg pylint
echo "Pylint score was $score"

# get html
pylint --load-plugins=pylint_json2html,pylint_django $files --output-format=jsonextended > pylint.json
pylint-json2html -f jsonextended -o public/pylint.html pylint.json

#cleanup
rm pylint.txt pylint.json

exit 0

