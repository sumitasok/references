module Company
  module Ibm
    module Buy
      extend Company::Default::Buy

      # def products(company, params = {})
      #   return "Company::Ibm::Buy.products #{company} #{params}"
      # end
    end
  end
end
# Ref: https://stackoverflow.com/questions/5487414/ruby-extend-module-inside-another-module?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
