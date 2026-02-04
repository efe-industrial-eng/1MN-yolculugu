import json
import matplotlib.pyplot as plt
import io
from PIL import Image, ImageDraw, ImageFont
import os

# --- AYARLAR ---
BANNER_WIDTH = 1600
BANNER_HEIGHT = 500
BG_COLOR = '#0a0a0a' # Koyu Siyah (Site teması)
GOLD_COLOR = '#ffcc00'
WHITE_COLOR = '#ffffff'
GREY_COLOR = '#cccccc'

def generate_banner():
    print("🎨 Banner generation starting...")
    
    # 1. Load data (data.json)
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
        # Get last 7 records (or all)
        recent_logs = data['gunluk_kayitlar'][-7:] if len(data['gunluk_kayitlar']) > 7 else data['gunluk_kayitlar']
        dates = [log['tarih'][5:] for log in recent_logs] # MM-DD format only
        earnings = [log['kazanc'] for log in recent_logs]
        total_earnings = data['toplam_kazanc']
        avg = total_earnings / len(data['gunluk_kayitlar']) if data['gunluk_kayitlar'] else 0
        print(f"📊 Data loaded. Total: ${total_earnings:,.0f}, Avg: ${avg:.1f}/Day")
    except FileNotFoundError:
        print("❌ Error: data.json not found!")
        return

    # 2. Create mini-chart with matplotlib (Dark theme)
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(6, 3.5), dpi=100)
    
    # Line and area
    ax.plot(dates, earnings, color=GOLD_COLOR, marker='o', linewidth=4, markersize=10, markerfacecolor=GOLD_COLOR, markeredgecolor=WHITE_COLOR)
    ax.fill_between(dates, earnings, color=GOLD_COLOR, alpha=0.2)
    
    # Title and axes
    ax.set_title(f'My Current Momentum: ${int(avg)}/Day Avg 🚀', color=GOLD_COLOR, fontsize=12, fontweight='bold', pad=15)
    ax.tick_params(axis='x', colors=GREY_COLOR, labelsize=9, rotation=30)
    ax.tick_params(axis='y', colors=GREY_COLOR, labelsize=9)
    ax.grid(color='#333', linestyle=':', linewidth=0.7)
    
    # Çerçeve Temizliği
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('#555')
    ax.spines['left'].set_color('#555')
    plt.tight_layout()

    # Grafiği hafızaya kaydet
    buf = io.BytesIO()
    plt.savefig(buf, format='png', transparent=True)
    buf.seek(0)
    chart_img = Image.open(buf)
    print("📉 Chart created.")

    # 3. Create main banner (PIL)
    banner = Image.new('RGB', (BANNER_WIDTH, BANNER_HEIGHT), color=BG_COLOR)
    draw = ImageDraw.Draw(banner)

    # Load fonts (try to find Arial on system)
    try:
        # Windows usually has it here
        font_path = "C:\\Windows\\Fonts\\arialbd.ttf" if os.name == 'nt' else "/Library/Fonts/Arial Bold.ttf"
        title_font = ImageFont.truetype(font_path, 70)
        sub_font = ImageFont.truetype(font_path, 35)
        stat_font = ImageFont.truetype(font_path, 28)
    except IOError:
        # Use default if not found (simpler appearance)
        print("⚠️ Warning: Arial font not found, using default font.")
        title_font = ImageFont.load_default()
        sub_font = ImageFont.load_default()
        stat_font = ImageFont.load_default()

    # --- SOL TARAF: METİNLER ---
    start_x = 80
    start_y = 100
    
    # Main Title
    draw.text((start_x, start_y), "INDUSTRIAL ENGINEER &", font=title_font, fill=WHITE_COLOR)
    
    # Subtitle
    draw.text((start_x, start_y + 170), "Data-Driven Efficiency | Python & Process Optimization", font=sub_font, fill=GREY_COLOR)
    
    # Gold Decorative Line
    draw.rectangle([(start_x, start_y + 230), (start_x + 250, start_y + 235)], fill=GOLD_COLOR)

    # Bottom Info (University & Statistics)
    draw.text((start_x, BANNER_HEIGHT - 120), "Yasar University Student 🎓", font=stat_font, fill=WHITE_COLOR)
    draw.text((start_x, BANNER_HEIGHT - 80), f"Live Status: ${total_earnings:,.0f} Processed in 3 Days", font=stat_font, fill=GOLD_COLOR)

    # --- RIGHT SIDE: CHART ---
    # Align chart to right
    chart_x = BANNER_WIDTH - chart_img.width - 50
    chart_y = (BANNER_HEIGHT - chart_img.height) // 2
    
    # Add subtle gold glow effect behind chart
    glow = Image.new('RGBA', (chart_img.width + 40, chart_img.height + 40), (255, 204, 0, 30))
    banner.paste(glow, (chart_x - 20, chart_y - 20), glow)
    
    # Paste chart
    banner.paste(chart_img, (chart_x, chart_y), chart_img)

    # 4. Save result
    output_filename = 'upwork_professional_banner.png'
    banner.save(output_filename)
    print(f"✅ Success! Banner saved: {output_filename}")
    
    # Cleanup
    buf.close()
    plt.close()

if __name__ == "__main__":
    generate_banner()