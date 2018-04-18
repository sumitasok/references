module Company
  module Accenture
    module Buy
      def products(company, params = {})
        return "Company::Accenture::Buy.products #{company} #{params}"
      end
    end
  end
end
