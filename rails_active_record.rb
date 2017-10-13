# https://chodounsky.net/2015/09/14/create-record-if-it-does-not-exist-in-activerecord/

User.find_or_create_by(first_name: "John", last_name: "Smith")
User.where(first_name: "John", last_name: "Smith").first_or_create

# bulk update
# https://stackoverflow.com/questions/4912510/rails-3-activerecord-the-best-way-to-mass-update-a-single-field-for-all-the

Model.where(phonenum: some_phone_number).update_all(hidden: true)