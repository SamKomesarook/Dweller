from ariadne import ObjectType, QueryType, gql, make_executable_schema
from ariadne.asgi import GraphQL

# Define types using Schema Definition Language (https://graphql.org/learn/schema/)
# Wrapping string in gql function provides validation and better error traceback
type_defs = gql("""
    type Query {
        status: String
    }
""")

# Map resolver functions to Query fields using QueryType
query = QueryType()

# Resolvers are simple python functions
@query.field("status")
def resolve_status(*_):
    return "Okay!"

# Create executable GraphQL schema
schema = make_executable_schema(type_defs, query)

# Create an ASGI app using the schema, running in debug mode
app = GraphQL(schema, debug=True)