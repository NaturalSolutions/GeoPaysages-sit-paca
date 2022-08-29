import models
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