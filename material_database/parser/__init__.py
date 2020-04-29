from .pyYamlParser import PyYamlParser
__all__ = ['PyYamlParser']


pars1=yp.YAMLParser("E:/YAML Parser/test.txt")
    
dict1=pars1.loadYAML(yamlText)
