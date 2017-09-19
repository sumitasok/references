# bulk update
# https://stackoverflow.com/questions/4912510/rails-3-activerecord-the-best-way-to-mass-update-a-single-field-for-all-the

Model.where(phonenum: some_phone_number).update_all(hidden: true)