# https://github.com/thoughtbot/factory_girl/blob/master/GETTING_STARTED.md






# trait
# https://stackoverflow.com/questions/30830034/using-a-default-trait-in-factorygirl-to-avoid-unnecessary-association-creation

factory :question_response do
  question
  work_history

  trait :open do
    question { FactoryGirl.create :question, question_type: 'open' }
  end
end

FactoryGirl.create :question_response, :open

# transient and factory

  factory :ecom_payment_with_orders, class: 'Ecom::Payment' do
    transient do
      user nil
      count 1
    end

    after(:create) do |payment, elevator|
      elevator.count.times do
        create(:ecom_order, buyer_id: elevator.user.id, payment_id: payment.id, user_payable: 100)
      end
    end
  end