
import logging as lg

class Task :

    lg.basicConfig(filename='task.log',level=lg.INFO, format= '%(levelname)s %(asctime)s %(message)s')

    def extract_list(self, l):
        """extract all the list entity"""
        try:
            lg.info('method extract_list started executing')
            for i in l:
                if type(i) == list:
                    lg.info(i)
                    if type(i) == set or type(i) == tuple or type(i) == dict:
                        for j in i:
                            if type(j) == list:
                                lg.info(j)
            lg.info('method extract_list has been executed')

        except Exception as e:
            lg.info('Error have occurred in execution of method extract_list')
            lg.error(e)

    def extract_dict(self, l):

        """extract all dict entity"""

        try:
            lg.info('method extract_dict started executing')
            for i in l:
                if type(i) == dict:
                    lg.info(i.items())
                    if type(i) == set or type(i) == tuple or type(i) == list:
                        for j in i:
                            if type(j) == dict:
                                lg.info(j.items())
            lg.info('method extract_dict has been executed')

        except Exception as e:
            lg.info('Error have occurred in execution of method extract_dict')
            lg.error(e)

    def extract_tuple(self, l):

        """extract all tuple entity"""

        try:
            lg.info('method extract_tuple started executing')
            for i in l:
                if type(i) == tuple:
                    lg.info(i)
                    if type(i) == set or type(i) == dict or type(i) == list:
                        for j in i:
                            if type(j) == tuple or type(j[1]) == tuple:
                                lg.info(j)
            lg.info('method extract_tuple has been successfully executed')

        except Exception as e:
            lg.info('Error have occurred in execution of method extract_dict')
            lg.error(e)

    def numerical_data_extract(self,l):

        """extract all the numerical data it may be part of dict key and values"""
        nd=[]
        try:
            lg.info('method numerical_data_extract started executing')
            for i in l:
                if type(i) == int:
                    nd.append(i)
                elif type(i) == list:
                    for j in i:
                        if type(j) == int:
                            nd.append(j)
                elif type(i) == tuple:
                    for j in i:
                        if type(j) == int:
                            nd.append(j)
                elif type(i) == set:
                    for j in i:
                        if type(j) == int:
                            nd.append(j)
                elif type(i) == dict:
                    for j in i.items():
                        if type(j[0]) == int:
                            nd.append(j[0])
                        if type(j[1]) == int:
                            nd.append(j[1])
            lg.info(nd)
            lg.info('method numerical_data_extract successfully executed')
        except Exception as e:
            lg.info('Error have occurred in execution of method numerical_data_extract')
            lg.error(e)

    def summation_numerical_values(self,l):

        """give summation of all the numerical values"""
        try:
            lg.info('method summation_numerical_values started executing')
            s = []
            for i in l:
                if type(i) == int:
                    s.append(i)
                elif type(i) == list:
                    for j in i:
                        if type(j) == int:
                            s.append(j)
                elif type(i) == tuple:
                    for j in i:
                        if type(j) == int:
                            s.append(j)
                elif type(i) == set:
                    for j in i:
                        if type(j) == int:
                            s.append(j)
                elif type(i) == dict:
                    for j in i.items():
                        if type(j[0]) == int:
                            s.append(j[0])
                        if type(j[1]) == int:
                            s.append(j[1])
            lg.info('sum of all numbers  %d', sum(s))
            lg.info('method summation_numerical_values successfully executed')
        except Exception as e:
            lg.info('Error have occurred in execution of method summation_numerical_values')
            lg.error(e)

    def extract_ineuron(self, l):

        """try to extract all the ineuron of data"""

        try:
            lg.info('method extract_ineuron started executing')
            for i in l:
                if i == 'ineuron':
                    lg.info('found it %s', i)
                elif type(i) == list:
                    for j in i:
                        if j == 'ineuron':
                            lg.info('found in list %s',j)
                elif type(i) == tuple:
                    for j in i:
                        if j == 'ineuron':
                            lg.info('found in tuple %s', j)
                elif type(i) == dict:
                    for j in i.items():
                        if j[0] == 'ineuron':
                            lg.info('found in dict %s',j[0])
                        if j[1] == 'ineuron':
                            lg.info('found in dict %s',j[1])
                elif type(i) == str:
                    for j in i:
                        if j == 'ineuron':
                            lg.info('found in string %s',j)
            lg.info('method extrcat_ineuron successfully executed')
        except Exception as e:
            lg.info('Error have occurred in execution of method extract_ineuron')
            lg.error(e)


    def number_of_occurence(self,l):
        """number of ocurences of all the data"""

        try:
            lg.info('method number_of_occurence started executing')
            oc = []
            for i in l:
                if type(i) == list:
                    for j in i:
                        oc.append(j)
                elif type(i) == tuple:
                    for j in i:
                        oc.append(j)
                elif type(i) == set:
                    for j in i:
                        oc.append(j)
                elif type(i) == dict:
                    for j in i.items():
                        oc.append(j[0])
                        oc.append(j[1])

            st = set(oc)  # st is set of unique element in list and oc is all the element in list
            for i in st:
                lg.info(i)
                lg.info('----> %d',oc.count(i),)
            lg.info('method number_of_occurence successfully executed')
        except Exception as e:
            lg.info('Error have occurred in execution of method number_of_occurence')
            lg.error(e)

    def number_keys(self, l):
        """find out number of keys in dict element"""

        try:
            lg.info('method number_keys started executing')
            count=0
            for i in l:
                if type(i)==dict:
                    lg.info(i.keys())
                    lg.info(len(i.keys()))
            lg.info('method number_keys successfully executed')
        except Exception as e:
            lg.info('Error have occurred in execution of method number_keys')
            lg.error(e)


    def string_data(self,l):
        """filter out all the string data"""

        try:
            lg.info('method string_data started executing')
            for i in l:
                if type(i) == str:
                    lg.info(i)
                elif type(i) == list:
                    for j in i:
                        if type(j) == str:
                            lg.info(j)
                elif type(i) == tuple:
                    for j in i:
                        if type(j) == str:
                            lg.info(j)
                elif type(i) == set:
                    for j in i:
                        if type(j) == str:
                            lg.info(j)
                elif type(i) == dict:
                    for j in i.items():
                        if type(j[0]) == str:
                            lg.info(j[0])
                        if type(j[1]) == str:
                            lg.info(j[1])
            lg.info('method string_data successfully executed')

        except Exception as e:
            lg.info('Error have occurred in execution of method string data')
            lg.error(e)

    def alphanum(self,l):
        """find out alphanum in data"""

        try:
            lg.info('method alphanum started executing')
            oc = []
            for i in l:
                if type(i) == list:
                    for j in i:
                        oc.append(j)
                elif type(i) == tuple:
                    for j in i:
                        oc.append(j)
                elif type(i) == set:
                    for j in i:
                        oc.append(j)
                elif type(i) == dict:
                    for j in i.items():
                        oc.append(j[0])
                        oc.append(j[1])

            for i in oc:
                if type(i) == str:
                    if i.isalnum():
                        lg.info(i)
            lg.info('method alphanum successfully executed')

        except Exception as e:
            lg.info('Error have occurred in execution of method alphanum')
            lg.error(e)


    def unwrap_data(self, l):
        """ unwrap all the data in list"""

        try:
            lg.info('method unwrap_data started executing')
            un = []
            for i in l:
                if type(i) == list:
                    for j in i:
                        un.append(j)
                elif type(i) == tuple:
                    for j in i:
                        un.append(j)
                elif type(i) == set:
                    for j in i:
                        un.append(j)
                elif type(i) == dict:
                    for j in i.items():
                        un.append(j[0])
                        un.append(j[1])

            lg.info(un)
            lg.info('method unwrap_data successfully executed')
        except Exception as e:
            lg.info('Error have occurred in execution of method unwrap_data')
            lg.error(e)

l=[[1,2,3,4,5],(2,3,4,5,6),(3,4,5,6,7),set([23,4,5,45,4,4,5,45,45,4,5]),{'k1':'sudh','k2':'ineuron','k3':'kumar',3:6,7:8},['ineuron','data science']]
obj = Task()
obj.extract_list(l)
obj.extract_dict(l)
obj.extract_tuple(l)
obj.extract_ineuron(l)
obj.summation_numerical_values(l)
obj.numerical_data_extract(l)
obj.number_of_occurence(l)
obj.string_data(l)
obj.number_keys(l)
obj.alphanum(l)
obj.unwrap_data(l)