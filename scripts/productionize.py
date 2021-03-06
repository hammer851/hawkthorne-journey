import os
import jinja2
import json
import version
import logging

MIXPANEL_DEV = 'ac1c2db50f1332444fd0cafffd7a5543'
MIXPANEL_TOKEN = os.environ.get('MIXPANEL_TOKEN', MIXPANEL_DEV)

def create_conf_lua(version):
    conf = json.load(open('src/config.json'))
    conf.update({
        "mixpanel": MIXPANEL_TOKEN,
        "title": "Journey to the Center of Hawkthorne v" + version,
        "iteration": version,
        "identity": "hawkthorne_release",
        "release": True,
    })

    with open('src/config.json', 'w') as f:
        json.dump(conf, f, indent=2, sort_keys=True)


def create_info_plist(version):
    template = jinja2.Template(open('templates/Info.plist').read())

    with open('osx/Info.plist', 'w') as f:
        f.write(template.render(version=version))


def main():
    v = version.next_version()

    logging.info("Creating osx/Info.plist")
    create_info_plist(v)

    logging.info("Creating src/config.json")
    create_conf_lua(v)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
