import random
from app.models import User, Role
from app import db

names = ['Musa', 'Abubakar', 'Abdullahi', 'Mohammed', 'Sani', 'Adamu', 'Usman', 'Umar', 'Muhammad', 'Muhammed', 'Aliyu', 'Yusuf', 'Ali', 'Garba', 'Bello', 'Haruna', 'Hassan', 'Lawal', 'Aminu', 'Yakubu', 'Isah', 'John', 'Idris', 'Eze', 'Yahaya', 'Salisu', 'Ahmed', 'Sunday', 'Akpan', 'Shehu', 'Isa', 'Amadi', 'Bala', 'Umaru', 'Ahmad', 'Okafor', 'Emmanuel', 'Saidu', 'Rabiu', 'Joseph', 'James', 'Okeke', 'Adebayo', 'Ojo', 'Samuel', 'Audu', 'Dauda', 'Okoro', 'Mustapha', 'Suleiman', 'Sulaiman', 'Okon', 'Baba', 'Peter', 'Muhammadu', 'Chukwu', 'Abba', 'Udo', 'Igwe', 'Ajayi', 'Jimoh', 'David', 'Daniel', 'Nwachukwu', 'Obi', 'Ugwu', 'Kabiru', 'Nwankwo', 'Sule', 'Salihu', 'Sale', 'Adam', 'Lawan', 'Dahiru', 'Okoye', 'Njoku', 'Nuhu', 'Bassey', 'Shuaibu', 'Okonkwo', 'Yau', 'Ado', 'Nura', 'Alhaji', 'Moses', 'Nasiru', 'Ogbonna', 'Hamza', 'Ayuba', 'Ismail', 'Suleman', 'Adeyemi', 'Nweke', 'Yunusa', 'Balogun', 'Azeez', 'Nwafor', 'Afolabi', 'Bukar', 'Effiong', 'Amadu', 'Magaji', 'Ani', 'Godwin', 'Mohammad', 'Samaila', 'Hussaini', 'Etim', 'Abu', 'Paul', 'Alhassan', 'Okorie', 'Sanusi', 'Gambo', 'Jibrin', 'Johnson', 'Kalu', 'Edet', 'Bashir', 'Anyanwu',
         'Alabi', 'Orji', 'Hamisu', 'Idowu', 'Danjuma', 'Nwosu', 'Monday', 'Udoh', 'Ohakwu', 'Opara', 'Salami', 'Abdu', 'Danladi', 'Kabir', 'Saleh', 'Shaibu', 'Taiwo', 'Dike', 'Auwal', 'Jamilu', 'Abdulahi', 'Agu', 'Solomon', 'Tukur', 'Sabo', 'Adeniyi', 'Onuoha', 'Ahmadu', 'Abdulkadir', 'Abdul', 'Lawali', 'Adeleke', 'Tijani', 'Ibe', 'Babatunde', 'Amos', 'Joshua', 'Buba', 'Jacob', 'Mamman', 'Agbo', 'Micheal', 'Murtala', 'Isaac', 'Eke', 'Uche', 'Edem', 'Muazu', 'Friday', 'Tanko', 'Michael', 'Babalola', 'Simon', 'Adekunle', 'Obasi', 'Chuku', 'Auwalu', 'Anthony', 'Saminu', 'Oke', 'Sanni', 'Mark', 'Owolabi', 'Ogbu', 'Mohammadu', 'Duru', 'Uba', 'Asuquo', 'Dada', 'Ezeh', 'Okoli', 'Thomas', 'Ogbonda', 'Umoh', 'Buhari', 'Gabriel', 'Aliu', 'Ismaila', 'Zubairu', 'Ganiyu', 'Edeh', 'Yusif', 'Inusa', 'Odo', 'Madu', 'Bawa', 'Inuwa', 'Iliya', 'Kareem', 'Kolawole', 'Raji', 'Zakari', 'Habibu', 'Iliyasu', 'Okechukwu', 'Ayodele', 'Stephen', 'Olatunji', 'Adewale', 'Bako', 'Sadiq', 'Jibril', 'Okoh', 'Adeyemo', 'George', 'Akinola', 'Ike', 'Samson', 'Bakare', 'Nnaji', 'Adeoye', 'Francis', 'Mathew', 'Essien', 'Okereke', 'Isiaka', 'Aisha', 'Abbas', 'Inyang']


def set_digits(n):
    range_start = 10 ** (n-1)
    range_end = (10 ** n) - 1
    return random.randint(range_start, range_end)


def set_name(names):
    full_name = (" ").join(random.choices(names, k=2))
    return full_name


def set_amount():
    return random.randint(10000, 9999999)


def set_transaction():
    transaction = {
        'ref_id': set_digits(7),
        'account_name': set_name(names),
        'account_number': set_digits(10),
        'amount': set_amount(),
        'trans_details': 'money for food'
    }
    return transaction


def set_user():
    user_info = {
        'first_name': random.choice(names),
        'last_name': random.choice(names),
        'username': None, # to e updated to first name
        'email': None, # to be updated to first_name.last_name@gmail.com
    }
    while user_info.get('username') in [user.username for user in User.query.all()] or user_info.get('username') is None:
        user_info['first_name']=random.choice(names)
        user_info['last_name'] = random.choice(names)
        user_info['username'] = user_info.get('first_name')+user_info.get('last_name')
    user_info['email']=user_info.get('first_name')+user_info.get('last_name')+'@titan.com'
    return user_info

def create_user(role_name):
    u = User(**set_user())
    u.set_password('12345678')
    u.role = Role.query.filter_by(role=role_name).first()
    db.session.add(u)


