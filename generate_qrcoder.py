import qrcode

# Informations de l'employé
nom = "Mouhamed"
prenom = "waw"
numero_telephone = "(+221) 78 371 84 72"
email = "mouhamed@gmail.com"
poste = "Responsable IT"
adresse = "Parcelle Assainie"
url_site_web = "https://wawtelecom.com"

# Créer le lien spécial pour les contacts
# lien_contacts = f"BEGIN:VCARD\nVERSION:3.0\nN:{nom};{prenom};;;\nFN:{prenom} {nom}\nORG:Waw Telecom;\nEMAIL;TYPE=INTERNET:{email}\nTEL;TYPE=CELL:{numero_telephone}\nEND:VCARD"
lien_contacts = f"BEGIN:VCARD\nVERSION:3.0\nN:{nom};{prenom};;;\nFN:{prenom} {nom}\nORG:Waw Telecom;\nEMAIL;TYPE=INTERNET:{email}\nTEL;TYPE=CELL:{numero_telephone}\nADR:;;{adresse};;;;\nURL:{url_site_web}\nEND:VCARD"
# Concaténer les informations
informations = f"Nom: {nom}\nPrénom: {prenom}\nTéléphone: {numero_telephone}\nEmail: {email}\nPoste occupé: {poste}\nAdresse: {adresse}\nSite Web: {url_site_web}\n\nScanner ce code ouvrirait l'application des contacts pour enregistrer le numéro de téléphone."

# Générer le QR code
qr = qrcode.QRCode(
   version=1,
   error_correction=qrcode.constants.ERROR_CORRECT_L,
   box_size=10,
   border=4,
)
qr.add_data(lien_contacts)
qr.make(fit=True)

# Sauvegarder le QR code dans un fichier
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode_mouhamed_2_waw.png")
