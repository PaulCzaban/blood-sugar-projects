import nightscout_api.Api as ns

api2 = ns.Api('http://czaban-nightscout.azurewebsites.net')

blood_sugar = round(api2.get_sgvs()[0].sgv / 18, 2)

print(f'My blood sugar level is: {blood_sugar} mmol/L')
