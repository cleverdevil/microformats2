def flatten_properties(items, is_outer=False):
    if isinstance(items, list):
        if len(items) < 1:
            return {}

        if len(items) == 1:
            item = items[0]
            if isinstance(item, dict):
                if 'type' in item:
                    props = {
                        'type': item.get('type', ['-'])[0].split('-')[1:][0]
                    }

                    properties = item.get("properties", {})
                    for prop in properties:
                        props[prop] = flatten_properties(properties[prop])

                    children = item.get('children', [])
                    if children:
                        if len(children) == 1:
                            props['children'] = [flatten_properties(children)]
                        else:
                            props['children'] = flatten_properties(children)
                    return props
                elif 'value' in item:
                    return item['value']
                else:
                    return ''
            else:
                return item
        elif is_outer:
            return {
                'children': [flatten_properties([child]) for child in items]
            }
        else:
            return [flatten_properties([child]) for child in items]
    else:
        return items


def to_jf2(mf2):
    jf2 = flatten_properties([mf2], is_outer=True)
    return jf2
