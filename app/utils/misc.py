# -*- coding: utf-8 -*-
import json
import os.path
import xml.sax.saxutils

import couchdb
import werkzeug
import werkzeug.routing
import werkzeug.utils
import mako.lookup

import app.widget
from app.config.generated import config

path = {}
path["root"] = os.path.join(os.path.dirname(__file__), "..")
path["static"] = os.path.join(path["root"], "../static")
path["templates"] = os.path.join(path["root"], "../templates")

local = werkzeug.Local()
local_manager = werkzeug.LocalManager([local])
application = local("application")

def db():
    return couchdb.Server(config["couchdb_server_url"])[config["couchdb_db"]]

template_lookup = mako.lookup.TemplateLookup(
    directories=[path["templates"]],
    input_encoding="utf-8",
    output_encoding="utf-8"
)

def url_for(endpoint, method=None, _external=False, **values):
    return local.url_adapter.build(endpoint, values, method=method, force_external=_external)

def template_response(templatename, **kwargs):
    kwargs["response"] = local.response
    local.response.data = template_render(templatename, **kwargs)

def template_render(templatename, **kwargs):
    template = template_lookup.get_template(templatename)
    kwargs.update({
        "url_for": url_for,
        "esc_attr": xml.sax.saxutils.quoteattr,
        "escape": xml.sax.saxutils.escape,
        "json": json.dumps,
        "endpoint": local.endpoint,
        "endpoint_override": None,
        "widget": app.widget
    })
    return template.render(**kwargs).decode("utf-8")

def redirect(endpoint, *args, **kwargs):
    local.response = werkzeug.utils.redirect(url_for(endpoint, *args, **kwargs))
