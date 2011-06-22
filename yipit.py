import sys
import urllib
import urllib2
import json


class yipit_deals(object):
    """A command line utility to search yipit deals"""

    api_key = 'zH4RS53tEN6C9PM5'
    yipit_api_url = 'http://api.yipit.com/v1/'
    deals_resource_path = 'deals/?'
    limit = 20

    params = {}

    def parse_inputs(self, args):
        """Receive comma seperated inputs from command line"""
        for arg in args:
            print arg
            key, value = arg.split('=')
            self.params[key] = value

    def sanitize_input(self):
        """Check for valid input params"""
        pass

    def api_call(self):
        """Make the actual API call"""
        url = self.yipit_api_url + self.deals_resource_path
        self.params['key'] = self.api_key
        url += urllib.urlencode(self.params)
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        return response.read()

    def parse_output(self, json_string):
        """Parse API json response"""
        deals = json.loads(json_string)
        return deals
        #check for meta here?

    def show_deals(self, deals):
        """Pretty output"""
        deals = deals[:self.limit]
        for deal in deals:
            print deal['title']

    def main(self, args):
        """Actual process"""
        self.parse_inputs(args)
        response = self.api_call()
        deals = self.parse_output(response)
        self.show_deals(deals['response']['deals'])

if __name__ == '__main__':
    y = yipit_deals()
    y.main(sys.argv[1:])
