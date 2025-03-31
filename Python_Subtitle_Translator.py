from deep_translator import GoogleTranslator  # type: ignore
import time

def translate_srt(input_file, output_file, batch_size=5):
    print("Načítám soubor titulků...")
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            subtitles = file.readlines()
        print(f"Načteno {len(subtitles)} řádků, začínám překlad...")
    except FileNotFoundError:
        print(f"❌ Chyba: Soubor {input_file} nebyl nalezen.")
        return
    
    translated_subtitles = []
    translator = GoogleTranslator(source="en", target="cs")
    
    total_lines = len(subtitles)
    progress_step = total_lines // 10  # Každých 10 % vypíšeme stav
    current_progress = 0

    text_block = []  # Blok pro dávkový překlad
    block_indices = []  # Seznam řádků patřících do aktuálního bloku
    subtitle_buffer = []  # Dočasné pole pro uchování bloků titulků

    for i, line in enumerate(subtitles, start=1):
        stripped_line = line.strip()
        
        if stripped_line.isdigit() or "-->" in stripped_line or stripped_line == "":
            # Pokud jde o číslo titulku, časovou značku nebo prázdný řádek, přidáme rovnou
            if text_block:
                # Přeložit nahromaděný blok textu
                try:
                    translated_texts = translator.translate("\n".join(text_block)).split("\n")
                    translated_subtitles.extend(translated_texts)
                except Exception as e:
                    print(f"⚠️ Chyba při překladu bloku (řádky {block_indices[0]}-{block_indices[-1]}): {e}")
                    translated_subtitles.extend(text_block)  # Zachovat původní text v případě chyby

                text_block = []  # Vyčistit blok
                block_indices = []  # Vyčistit seznam řádků
                time.sleep(1)  # Pauza 1 sekunda mezi bloky
            
            translated_subtitles.append(line)  # Zachovat formátování (číslování, časové značky)
        else:
            # Sbírat řádky, které patří do titulků (kromě číslování a časových značek)
            text_block.append(stripped_line)
            block_indices.append(i)

        # Výpis průběhu překladu každých 10 %
        if i >= current_progress + progress_step:
            print(f"✅ Přeloženo {round(i / total_lines * 100)} %")
            current_progress = i

    try:
        with open(output_file, "w", encoding="utf-8") as file:
            file.writelines(line + "\n" for line in translated_subtitles)
        print(f"🎉 Překlad dokončen! Přeložené titulky uloženy do: {output_file}")
    except Exception as e:
        print(f"❌ Chyba při ukládání souboru: {e}")

# Použití
input_srt = r"D:\Download\Dog.Man.2025.1080p.WEB.h264-ETHEL\Dog.Man.2025.1080p.WEB.h264-ETHEL.srt"
output_srt = r"D:\Download\Dog.Man.2025.1080p.WEB.h264-ETHEL\Dog.Man.2025.CZ.srt"
translate_srt(input_srt, output_srt)
