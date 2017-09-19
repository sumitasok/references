# https://stackoverflow.com/questions/17918430/rspec-stub-method-that-is-in-the-controller

CompaniesController.any_instance.stub(:validates_fbid).and_return('companyid')

# https://stackoverflow.com/questions/9322353/factory-girl-create-that-bypasses-my-model-validation

describe ".current" do
  let!(:current_group) { FactoryGirl.create(:group) }
  let!(:old_group) {
    g = FactoryGirl.build(:group, :expiry => Time.now - 3.days)
    g.save(:validate => false)
    g
  }

  specify { Group.current.should == [current_group] }
end

# https://relishapp.com/rspec/rspec-expectations/docs/built-in-matchers/be-matchers

RSpec.describe "be_truthy matcher" do
  specify { expect(true).to be_truthy }
  specify { expect(7).to be_truthy }
  specify { expect("foo").to be_truthy }
  specify { expect(nil).not_to be_truthy }
  specify { expect(false).not_to be_truthy }

  # deliberate failures
  specify { expect(true).not_to be_truthy }
  specify { expect(7).not_to be_truthy }
  specify { expect("foo").not_to be_truthy }
  specify { expect(nil).to be_truthy }
  specify { expect(false).to be_truthy }
end

# https://apidock.com/ruby/Object/instance_variable_set

class Fred
  def initialize(p1, p2)
    @a, @b = p1, p2
  end
end
fred = Fred.new('cat', 99)
fred.instance_variable_set(:@a, 'dog')   #=> "dog"
fred.instance_variable_set(:@c, 'cat')   #=> "cat"
fred.inspect 

# https://stackoverflow.com/questions/13879700/rails-model-valid-flushing-custom-errors-and-falsely-returning-true

rails active record model .valid? clears the custome error messages.

# https://robots.thoughtbot.com/ruby-2-keyword-arguments
# Key word arguments

def foo(bar: 'default')
  puts bar
end

foo # => 'default'
foo(bar: 'baz') # => 'baz'

# http://guides.rubyonrails.org/active_record_validations.html#valid-questionmark-and-invalid-questionmark
class GoodnessValidator < ActiveModel::Validator
  def validate(record)
    if record.first_name == "Evil"
      record.errors[:base] << "This person is evil"
    end
  end
end
 
class Person < ApplicationRecord
  validates_with GoodnessValidator
end

class Person < ApplicationRecord
  validates :name, presence: true
end
 
>> Person.new.errors[:name].any? # => false
>> Person.create.errors[:name].any? # => true
>> p.errors.messages
# => {name:["can't be blank"]}