import gradio as gr

# رابط Colab الرسمي:
colab_url = "https://colab.research.google.com/drive/1xQOSRGNMVcALfc3aC9flchtJZfObQusQ8"

def open_colab():
    return f"🚀 [Click here to run the Full NanoDockPredictor Notebook in Colab]({colab_url})"

iface = gr.Interface(
    fn=open_colab,
    inputs=[],
    outputs="markdown",
    title="🧬 NanoDockPredictor - Official Tool (Full Version)",
    description="""
    ✅ Smart Docking of Proteins and Ligands  
    ✅ AutoDock Vina + OpenBabel + Gaussian Input Generator  
    ---
    👉 The Full version runs in Google Colab — click below to launch:
    """
)

iface.launch()
