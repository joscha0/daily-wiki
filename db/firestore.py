import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

certificate = {
    "type": "service_account",
    "project_id": "daily-wiki-newsletter",
    "private_key_id": os.environ['private_key_id'],
    "private_key": os.environ['private_key'].replace('\\n', '\n'),
    "client_email": os.environ['client_email'],
    "client_id": os.environ['client_id'],
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": os.environ['client_x509_cert_url']
}

cred = credentials.Certificate(certificate)
firebase_admin.initialize_app(cred)

db = firestore.client()


def adduser(email, lang):
    doc_ref = db.collection(u'emails').document(email)
    if doc_ref.get().exists:
        return False
    else:
        doc_ref.set({
            u'confirmed': False,
            u'language': lang
        })
        return True


def getusers():
    users_ref = db.collection(u'emails')
    docs = users_ref.stream()
    data = {}

    for doc in docs:
        data[doc.id] = doc.to_dict()

    return data


def validateuser(email):
    doc_ref = db.collection(u'emails').document(email)
    if doc_ref.get().exists:
        doc_ref.update({
            u'confirmed': True,
        })
        return True
    else:
        return False


def deluser(email):
    doc_ref = db.collection(u'emails').document(email)
    if doc_ref.get().exists:
        doc_ref.delete()
        return True
    else:
        return False


if __name__ == "__main__":
    print(adduser("joschavonandrian@gmail.com", "en"))
    print(getusers())
    print(validateuser("joschavonandrian@gmail.com"))
    print(deluser("test@960.eu"))
