import sys
import urllib
import urllib2
import json
import re


class YipitDeals(object):
    """A command line utility to search yipit deals"""

    api_key = 'zH4RS53tEN6C9PM5'
    yipit_api_url = 'http://api.yipit.com/v1/'
    deals_resource_path = 'deals'

    params = {}

    def parse_inputs(self, args):
        """Receive comma seperated inputs from command line"""
        for arg in args:
            if(arg.count('=') == 1):
                key, value = arg.split('=')
                if self.validate_input(key, value):
                    self.params[key] = value
            else:
                print 'Skipping', arg

    def validate_input(self, key, value):
        """Check for valid input params"""
        valid_params = {
            'lat' : {
                'data_type' : 'float',
                'maxlen' : 11
                },
            'lon' : {
                'data_type' : 'float',
                'maxlen' : 11
                },
            'radius' : {
                'data_type' : 'float',
                'maxlen' : 11
                },
            'division' : {
                'data_type' : 'slug',
                'maxlen' : 20
                },
            'source' : {
                'data_type' : 'slug',
                'maxlen' : 20
                },
            'phone' : {
                'data_type' : 'numeric',
                'maxlen' : 11
                },
            'tag' : {
                'data_type' : 'slug',
                'maxlen' : 20
                },
            'paid' : {
                'data_type' : 'bool',
                'maxlen' : 5
                },
            'limit' : {
                'data_type' : 'float',
                'maxlen' : 4
                }
            }
        if key in valid_params.keys():
            data_type = valid_params[key]['data_type']
            if data_type == 'float':
                try:
                    float(value)
                except:
                    return False
            elif data_type == 'slug':
                if not re.match("^[A-Za-z-,]*$", value):
                    return False
            elif data_type == 'numeric':
                if not value.isdigit():
                    return False
            elif data_type == 'bool':
                if not value.lower() in ['0', '1', 'true', 'false']:
                    return False
            maxlen = valid_params[key]['maxlen']
            if len(value) > maxlen:
                return False
            return True  # Validation Complete
        else:
            print 'Invalid param', key
            return False

    def build_deals_url(self):
        """Construct URL with get params"""
        url = self.yipit_api_url + self.deals_resource_path
        self.params['key'] = self.api_key
        url += '?' + urllib.urlencode(self.params)
        return url

    def get_contents(self, url):
        """Make the actual API call"""
        req = urllib2.Request(url)
        try:
            response = urllib2.urlopen(req)
            return response.read()
        except urllib2.URLError, (err):
            print "URL error(%s)" % (err)
            return None

    def parse_output(self, json_string):
        """Parse API json response"""
        deals = json.loads(json_string)
        return deals['response']['deals']
        #check for meta here?

    def show_deals(self, deals):
        """Pretty output"""
        if deals:
            for deal in deals:
                print deal['title']
        else:
            print 'No deals found'

    def main(self, args):
        """Actual process"""
        self.parse_inputs(args)
        deals_url = self.build_deals_url()
        response = self.get_contents(deals_url)
        if response:
            deals = self.parse_output(response)
            self.show_deals(deals)
            return deals

if __name__ == '__main__':
    y = YipitDeals()
    y.main(sys.argv[1:])
