from django.shortcuts import render

posts = {
        "post1":"ahoi ohowh eofh eoyh wo;f;howhofuh wowhof wuiifowolyw fowyw oiiwo",
        "post2":"dsuofh owef hafh q ouer ljergoiro segriuehig riliuerhdh  hl sudh",
        "post3":"wiuy iwbdkc  eowh whfh doyeo ehiu ugfkuflsyiger yeriwye iugh eirhirluhlehurhl t rty",
        "post4":"oqer  weytytr twoir t gfbkfg irt irhrohthut su wiwfisyfgw uweigwig iwur wigi"
    }

# Create your views here.
def post(request, post):
    post_key = post
    post_val = posts[post_key]
    return render(request, "blog_pages\post.html", {"post_key":post_key, "post_val":post_val})

def posts(request):
    return render(request, "blog_pages\posts.html", {"posts" : posts})

def index(request):
    return render(request, "blog_pages\index.html")
