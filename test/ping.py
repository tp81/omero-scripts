# Ping script, Jython edition
import omero, omero.scripts as script

client = script.client("ping.py", "simple ping script",
         script.Long("a"), script.String("b"))

keys = client.getInputKeys()
print "Keys found:"
print keys
for key in keys:
      client.setOutput(key, client.getInput(key))
	  
client.closeSession()
