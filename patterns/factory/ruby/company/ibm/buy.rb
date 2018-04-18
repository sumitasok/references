module Company
  module Ibm
    module Buy
      def products(company, params = {})
        return "Company::Ibm::Buy.products #{company} #{params}"
      end
    end
  end
end
