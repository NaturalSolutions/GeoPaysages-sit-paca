from flask import render_template, Blueprint
import models
import utils

custom = Blueprint('custom', __name__)

observatory_schema_lite = models.ObservatorySchemaLite(many=True)

def getFooterData():
    observatories = models.Observatory.query.filter(models.Observatory.is_published == True).order_by(models.Observatory.title)
    return {
        'observatories': observatory_schema_lite.dump(observatories)
    }

def custom_inject_to_tpl():
    return dict(
        getFooterData= getFooterData
    )

@custom.route('/about')
def about():
    return render_template(utils.getCustomTpl('about'))