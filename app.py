from flask import Flask
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.ext.flask.flask_middleware import FlaskMiddleware
from opencensus.trace.samplers import ProbabilitySampler

app = Flask(__name__)

# Set up Application Insights exporter
middleware = FlaskMiddleware(
    app,
    exporter=AzureExporter(connection_string='InstrumentationKey=99ff427e-6f0a-429c-b87c-6760b062e5cb;IngestionEndpoint=https://ukwest-0.in.applicationinsights.azure.com/;LiveEndpoint=https://ukwest.livediagnostics.monitor.azure.com/;ApplicationId=11d7eeb3-bd20-4ce8-8c0e-7c77af344ffe'),
    sampler=ProbabilitySampler(1.0)
)

@app.route('/')
def hello():
    return 'Hello, world! This is my Azure DevOps-style deployment.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)





