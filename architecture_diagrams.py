"""
create a list of json objects in a python file to store architecture diagrams
json object format should be [{'name':"",'image_url':"",'source':"",'type':""}]
"""

diagrams = [
        {
            'name':"real time monitoring and debugging",
            'image_url':"https://drive.google.com/uc?id=1zrjxYfzxXShJL_7rEyQsdu5vfUTR_MLQ&export=download",
            'source':"https://bytes.swiggy.com/architecture-and-design-principles-behind-the-swiggys-delivery-partners-app-4db1d87a048a",
            'type':"block"
        },
        {
            'name':"celery queue",
            'image_url':"https://drive.google.com/uc?id=1XKhlgLisXHwI74BkpE_KgVEpaXovfS_p&export=download",
            'source':"https://cloud.google.com/blog/products/data-analytics/scale-your-composer-environment-together-your-business",
            'type':"block"
        },
        {
            'name':"real time historical logs",
            'image_url':"https://drive.google.com/uc?id=1sXlNSw6L2FBbCoAfmC4tmbAXrrFo63DY&export=download",
            'source':"https://bytes.swiggy.com/architecture-and-design-principles-behind-the-swiggys-delivery-partners-app-4db1d87a048a",
            'type':"block"
        },
        {
            'name':"poor network scenarios",
            'image_url':"https://drive.google.com/uc?id=1RjVPch1nOVSKuq3bstp50ZfTjJJNdxA3&export=download",
            'source':"https://bytes.swiggy.com/architecture-and-design-principles-behind-the-swiggys-delivery-partners-app-4db1d87a048a",
            'type':"block"
        },
        {
            'name':"aws lamda",
            'image_url':"https://drive.google.com/uc?id=1EAN2HP4qaf0iYipaibG4URdIb9FJp3gf&export=download",
            'source':"https://aws.amazon.com/blogs/architecture/architecting-a-low-cost-web-content-publishing-system/",
            'type':"block"
        },
        {
            'name':"order management",
            'image_url':"https://drive.google.com/uc?id=1Lw5NRYvKE6feosrls4P7lr1nlgoyf-_l&export=download",
            'source':"https://bytes.swiggy.com/architecture-and-design-principles-behind-the-swiggys-delivery-partners-app-4db1d87a048a",
            'type':"block"
        },
        {
            'name':"reddis twitter",
            'image_url':"https://drive.google.com/uc?id=1u2eTu1bij3u-3szwfAT4Ubg4Pm5-vd4R&export=download",
            'source':"https://medium.com/@narengowda/system-design-for-twitter-e737284afc95",
            'type':"block"
        },
        {
            'name':"swiggy data flow",
            'image_url':"https://drive.google.com/uc?id=1gNxTg2pFJAYy9AmG-hFqmpxwVbHZ8UfQ&export=download",
            'source':"https://bytes.swiggy.com/architecture-and-design-principles-behind-the-swiggys-delivery-partners-app-4db1d87a048a",
            'type':"block"
        },
        {
            'name':"swiggy partners",
            'image_url':"https://drive.google.com/uc?id=1O8q19or1i778mYvoHPpFqhQN19UD83Ib&export=download",
            'source':"https://bytes.swiggy.com/architecture-and-design-principles-behind-the-swiggys-delivery-partners-app-4db1d87a048a",
            'type':"block"
        },
        {
            'name':"twitter system design",
            'image_url':"https://drive.google.com/uc?id=1PdPV4NIL7ELn1Ojr9NuNecxLCqoX_qfB&export=download",
            'source':"https://medium.com/@narengowda/system-design-for-twitter-e737284afc95",
            'type':"block"
        }
    ]




if __name__ == "__main__": 
    print ("Here is the list diagrams: %s" %diagrams) 
