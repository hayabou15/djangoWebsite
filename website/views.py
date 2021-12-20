from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        ctxt  = super().get_context_data()
        ctxt["username"] = "あ"
        return ctxt


class AboutView(TemplateView):
    template_name = "about.html"
    
    def get_context_data(self):
        ctxt  = super().get_context_data()
        ctxt["studytime"] = 256
        ctxt["skills"] = [
            "Python",
            "Django",
            "flask",
        ]

        return ctxt
