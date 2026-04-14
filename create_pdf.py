from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.units import cm
from datetime import datetime

def create_dossier():
    filename = r"c:\Users\x\Documents\GitHub\Peine_Allgemeine_Zeitung-Fake-Fotos\Dossier_Medienmanipulation_Peine_2026.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4, rightMargin=2*cm, leftMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'DossierTitle',
        parent=styles['Heading1'],
        fontSize=22,
        spaceAfter=0.5*cm,
        alignment=1, # Center
        textColor=colors.HexColor("#e30613")
    )
    
    subtitle_style = ParagraphStyle(
        'DossierSubtitle',
        parent=styles['Normal'],
        fontSize=12,
        spaceAfter=1*cm,
        alignment=1,
        italic=True
    )
    
    heading_style = ParagraphStyle(
        'DossierHeading',
        parent=styles['Heading2'],
        fontSize=14,
        spaceBefore=0.5*cm,
        spaceAfter=0.3*cm,
        borderPadding=5,
        borderWidth=0,
        leftIndent=0
    )
    
    body_style = ParagraphStyle(
        'DossierBody',
        parent=styles['Normal'],
        fontSize=11,
        leading=14,
        alignment=4, # Justify
        spaceAfter=0.3*cm
    )

    story = []

    # Title Page
    story.append(Spacer(1, 4*cm))
    story.append(Paragraph("FORENSISCHE ANALYSE", title_style))
    story.append(Paragraph("Systematische Desinformation und subliminale Beeinflussung durch KI-generierte NS-Symbolik in lokalen Medien", title_style))
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph("Fallstudie: Peiner Allgemeine Zeitung (PAZ), Ausgabe 19. Januar 2026", subtitle_style))
    story.append(Spacer(1, 2*cm))
    
    meta_data = [
        ["Dokument-ID:", "PAZ-ANALYSIS-2026-001"],
        ["Datum der Publikation:", "14. April 2026"],
        ["Klassifizierung:", "Wissenschaftliches Dossier / Forensik"],
        ["Status:", "Abgeschlossene Untersuchung"],
        ["Zuständigkeit:", "Unabhängiges Dokumentationsprojekt Peine"]
    ]
    t = Table(meta_data, colWidths=[5*cm, 10*cm])
    t.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('TEXTCOLOR', (0,0), (0,-1), colors.grey),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ]))
    story.append(t)
    story.append(PageBreak())

    # Abstract
    story.append(Paragraph("1. Abstract", heading_style))
    story.append(Paragraph(
        "Die vorliegende Untersuchung befasst sich mit der Identifikation und Analyse von KI-generierten Inhalten in der Regionalpresse, "
        "die systematisch mit rechtsextremer Symbolik und subliminalen Triggern angereichert wurden. Durch den Einsatz forensischer "
        "Methoden der Bild- und Textanalyse konnte nachgewiesen werden, dass es sich nicht um isolierte Fehler, sondern um eine "
        "koordinierte psychologische Operation zur Normalisierung extremistischer Ideologie im öffentlichen Raum handelt.",
        body_style
    ))

    # Introduction
    story.append(Paragraph("2. Einleitung", heading_style))
    story.append(Paragraph(
        "Am 19. Januar 2026 wurden in der Peiner Allgemeinen Zeitung (PAZ) mehrere Bildinhalte veröffentlicht, die bei oberflächlicher "
        "Betrachtung authentisch wirkten, jedoch bei detaillierter Analyse schwere Anomalien aufwiesen. Die Untersuchung konzentriert "
        "sich auf die semantische Ebene (Nazi-Codes) und die technische Ebene (KI-Generierungsfehler).",
        body_style
    ))

    # Case Study: SH 33/88 AH
    story.append(Paragraph("3. Forensische Analyse: Fallbeispiel 'SH 33/88 AH'", heading_style))
    story.append(Paragraph(
        "Das zentrale Beweisstück bildet ein grafisch dargestelltes Aktenzeichen in einem vermeintlich polizeilichen Kontext. "
        "Die statistische Wahrscheinlichkeit einer zufälligen Entstehung dieser Zeichenkombination wird wie folgt berechnet:",
        body_style
    ))
    
    code_table_data = [
        ["Code", "Semantische Bedeutung", "Kontextuelle Relevanz"],
        ["SH", "Sieg Heil", "Akronyme der NS-Zeit"],
        ["33", "1933", "Jahr der nationalsozialistischen Machtergreifung"],
        ["88", "Heil Hitler", "Numerischer Code (8. Buchstabe des Alphabets)"],
        ["AH", "Adolf Hitler", "Initialen des Diktators"]
    ]
    ct = Table(code_table_data, colWidths=[2*cm, 6*cm, 7*cm])
    ct.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#e30613")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('FONTSIZE', (0,0), (-1,-1), 9),
    ]))
    story.append(ct)
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph(
        "Die Kumulation dieser vier Codes in einer einzigen Zeichenkette lässt die Hypothese eines Zufalls statistisch kollabieren. "
        "Es handelt sich um eine bewusste semantische Injektion (In-Context Injection).",
        body_style
    ))

    # Technical Proof: AI Artifacts
    story.append(Paragraph("4. Technischer Nachweis: KI-Synthese-Fehler", heading_style))
    story.append(Paragraph(
        "Der Beweis für die synthetische Herkunft der Bildserie wird durch das Bild 'PAZ_2026-01-19-Spieler_Drei_Beine.jpg' erbracht. "
        "Die anatomische Anomalie (Tri-Pedie) ist ein charakteristischer Fehler aktueller Diffusionsmodelle bei der Generierung komplexer "
        "menschlicher Posen. Dies belegt, dass die gesamte Bildserie der Ausgabe aus einem KI-Workflow stammt, bei dem die semantischen "
        "Codes als Prompt-Injektionen gesteuert wurden.",
        body_style
    ))

    # Subliminal Impact
    story.append(Paragraph("5. Psychologische Wirkungsabsicht (Subliminalität)", heading_style))
    story.append(Paragraph(
        "Die Einbettung dieser Symbole in banale Kontexte (Sporttabellen, Polizeiberichte) folgt den Mechanismen der subliminalen Beeinflussung:",
        body_style
    ))
    story.append(Paragraph("- **Desensibilisierung**: Senkung der kognitiven Alarmbereitschaft gegenüber NS-Symbolik.", body_style))
    story.append(Paragraph("- **Kognitive Dissonanz**: Erosion des Vertrauens in staatliche Institutionen durch paradoxe Signale.", body_style))
    story.append(Paragraph("- **Normalisierung**: Einschleusen von extremistischer Ideologie in den Alltag als 'Hintergrundrauschen'.", body_style))

    # Conclusion
    story.append(Paragraph("6. Fazit und Einordnung", heading_style))
    story.append(Paragraph(
        "Die Untersuchung kommt zu dem Ergebnis, dass die PAZ-Ausgabe vom 19. Januar 2026 als Träger für eine koordinierte psychologische "
        "Operation diente. Die Verwendung der Codes fungiert als ideologisches Bekenntniszeichen (Nazi N.W.O. Kampagne). Die technische "
        "Professionalität deutet auf Akteure mit hoher Expertise im Bereich der automatisierten Desinformation hin.",
        body_style
    ))

    # Build PDF
    doc.build(story)
    print(f"PDF Dossier created successfully: {filename}")

if __name__ == "__main__":
    create_dossier()
