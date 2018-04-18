module Company
  module Default
    module Buy
      def products(company, params = {})
        return "Company::Default::Buy.products #{company} #{params}"
      end
    end
  end
end
