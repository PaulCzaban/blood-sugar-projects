import nightscout_api.Api as ns

api2 = ns.Api('http://czaban-nightscout.azurewebsites.net')

blood_sugar = api2.get_sgvs()[0].sgv

print(f'My blood sugar level is: {blood_sugar} mmol/L')
