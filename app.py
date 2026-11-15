import gradio as gr
from text_analyzer import get_entities

text_1 = "Президент України Володимир Зеленський зустрівся з представниками Європейської комісії у Києві."
text_2 = "Під час подорожі до Італії, Аліса відвідала Рим та Флоренцію. У Римі вона відвідала Колізей та Ватикан, а у Флоренції — галерею Уффіці."
text_3 = "10 жовтня 2025 року відбувся саміт ООН, а ЄС прийняв важливу постанову."

theme = gr.themes.Soft(
    primary_hue="purple",
    secondary_hue="indigo",
    neutral_hue="slate",
)

with gr.Blocks(theme=theme) as demo:
    gr.Markdown("<h1 align='center'> Знаходження власних назв в українському тексті</h1>")
    gr.Markdown(
        "Цей застосунок <i>допоможе</i> вам знайти <b>власні назви (імена, місця, організації та інше)</b> в українському тексті. Все, що вам потрібно — <b><i>ввести текст</i></b> та <b><i>натиснути на кнопку</i></b>😉"
    )
    
    with gr.Row():
        with gr.Column():
            txt_input = gr.Textbox(
                label="Вхідний текст:",
                placeholder="Введіть текст українською (Наприклад: Київ - столиця України): ",
                lines=5,
            )
            
            with gr.Row():
                btn_clear = gr.Button("Очистити поле🗑️", variant="secondary")
                btn_submit = gr.Button("Знайти🔍", variant="primary")
            
            gr.Markdown("### 📄 Швидкі тестові приклади:")
            with gr.Row():
                btn_test1 = gr.Button("Тест 1")
                btn_test2 = gr.Button("Тест 2")
                btn_test3 = gr.Button("Тест 3")
                
        with gr.Column():
            out_output = gr.HighlightedText(
                label="Розпізнані власні назви 📑:",
                color_map={
                    "PER": "red",
                    "LOC": "green",
                    "ORG": "purple",
                    "MISC": "orange",
                },
            )

    btn_submit.click(fn=get_entities, inputs=txt_input, outputs=out_output)
    btn_clear.click(fn=lambda: ("", []), inputs=None, outputs=[txt_input, out_output])
    
    btn_test1.click(fn=lambda: (text_1, get_entities(text_1)), inputs=None, outputs=[txt_input, out_output])
    btn_test2.click(fn=lambda: (text_2, get_entities(text_2)), inputs=None, outputs=[txt_input, out_output])
    btn_test3.click(fn=lambda: (text_3, get_entities(text_3)), inputs=None, outputs=[txt_input, out_output])

if __name__ == "__main__":
    demo.launch()
    