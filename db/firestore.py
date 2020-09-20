import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate(
    'db/daily-wiki-newsletter-firebase-adminsdk-saicz-bd75679ae4.json')
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
