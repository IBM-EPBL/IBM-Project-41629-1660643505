from ibm_watson_machine_learning import APIClient

web_cred={
    "apikey": "6PcwxslwN5BT5dP8C4oKx62Vsz661Sxw-KY3oVAygalC",
	"url": "https://eu-gb.ml.cloud.ibm.com"
}

client=APIClient(web_cred)
spaceID="e4ef5efc-e11a-41cc-9c1e-b45c6a510aeb"
x=client.set.default_space(spaceID)
print(x)