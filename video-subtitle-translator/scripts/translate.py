#!/usr/bin/env python3
"""
多语言字幕翻译器
支持字幕提取、翻译、生成双语字幕文件
"""

import json
import re
from datetime import datetime
from typing import List, Dict, Optional

# 支持的语言
LANGUAGES = {
    "zh": "中文简体",
    "zh-tw": "中文繁体",
    "en": "英语",
    "ja": "日语",
    "ko": "韩语",
    "fr": "法语",
    "de": "德语",
    "es": "西班牙语",
    "pt": "葡萄牙语",
    "ru": "俄语",
    "ar": "阿拉伯语",
    "vi": "越南语",
    "th": "泰语",
    "id": "印尼语",
    "ms": "马来语",
    "hi": "印地语"
}

# 字幕样式
SUBTITLE_STYLES = {
    "classic": {
        "name": "经典白字黑边",
        "description": "白色字体，黑色描边，最通用"
    },
    "modern": {
        "name": "现代简约",
        "description": "白色半透明背景，圆角字体"
    },
    "highlight": {
        "name": "高亮重点",
        "description": "关键词高亮显示"
    },
    "karaoke": {
        "name": "卡拉OK效果",
        "description": "逐字变色动画效果"
    }
}

# 字幕格式
SUBTITLE_FORMATS = ["srt", "ass", "vtt", "txt"]

class SubtitleEntry:
    """字幕条目"""
    def __init__(self, index: int, start: str, end: str, text: str):
        self.index = index
        self.start = start
        self.end = end
        self.text = text
    
    def to_srt(self) -> str:
        """转为SRT格式"""
        return f"{self.index}\n{self.start} --> {self.end}\n{self.text}\n"
    
    def to_ass(self) -> str:
        """转为ASS格式"""
        return f"Dialogue: 0,{self.start},{self.end},Default,,0,0,0,,{self.text}"
    
    def to_vtt(self) -> str:
        """转为VTT格式"""
        return f"{self.start} --> {self.end}\n{self.text}\n"

def parse_srt(content: str) -> List[SubtitleEntry]:
    """解析SRT字幕"""
    entries = []
    blocks = re.split(r'\n\n+', content.strip())
    
    for block in blocks:
        lines = block.strip().split('\n')
        if len(lines) >= 3:
            try:
                index = int(lines[0])
                time_line = lines[1]
                start, end = time_line.split(' --> ')
                text = '\n'.join(lines[2:])
                entries.append(SubtitleEntry(index, start.strip(), end.strip(), text))
            except (ValueError, IndexError):
                continue
    
    return entries

def translate_text(text: str, target_lang: str, source_lang: str = "auto") -> str:
    """
    模拟翻译功能
    
    在实际使用中，这里应该调用真实的翻译API
    如：Google Translate API、DeepL、百度翻译等
    """
    # 模拟翻译结果
    translations = {
        "en": {
            "你好": "Hello",
            "欢迎": "Welcome",
            "感谢观看": "Thanks for watching",
            "今天": "Today",
            "分享": "Share"
        }
    }
    
    if target_lang in translations:
        for cn, en in translations[target_lang].items():
            if cn in text:
                text = text.replace(cn, en)
    
    return f"[翻译{target_lang}]{text}"

def generate_dual_subtitle(entry: SubtitleEntry, source_text: str, target_text: str, layout: str = "vertical") -> str:
    """生成双语字幕"""
    if layout == "vertical":
        # 上下排列
        return f"{source_text}\n{target_text}"
    else:
        # 左右排列
        return f"{source_text} | {target_text}"

def translate_subtitle_file(
    input_file: str,
    source_lang: str = "auto",
    target_lang: str = "zh",
    output_format: str = "srt",
    dual: bool = False,
    style: str = "classic"
) -> dict:
    """
    翻译字幕文件
    
    Args:
        input_file: 输入字幕文件路径
        source_lang: 源语言
        target_lang: 目标语言
        output_format: 输出格式
        dual: 是否生成双语字幕
        style: 字幕样式
    """
    result = {
        "input_file": input_file,
        "source_lang": source_lang,
        "target_lang": target_lang,
        "output_format": output_format,
        "dual": dual,
        "style": style,
        "generated_at": datetime.now().isoformat(),
        "entries": [],
        "output_files": []
    }
    
    # 读取输入文件（这里模拟读取）
    sample_entries = [
        SubtitleEntry(1, "00:00:01,000", "00:00:05,000", "大家好，欢迎来到我的频道"),
        SubtitleEntry(2, "00:00:06,000", "00:00:10,000", "今天我要分享一些实用技巧"),
        SubtitleEntry(3, "00:00:11,000", "00:00:15,000", "希望对你们有帮助"),
        SubtitleEntry(4, "00:00:16,000", "00:00:20,000", "如果喜欢的话，记得点赞关注哦")
    ]
    
    for entry in sample_entries:
        translated = translate_text(entry.text, target_lang, source_lang)
        translated_entry = SubtitleEntry(entry.index, entry.start, entry.end, translated)
        
        result["entries"].append({
            "index": entry.index,
            "time_range": f"{entry.start.split(',')[0]} - {entry.end.split(',')[0]}",
            "source": entry.text,
            "target": translated
        })
        
        # 生成输出文件路径
        if dual:
            result["output_files"].append({
                "file": f"{input_file}_{target_lang}_dual.{output_format}",
                "preview": generate_dual_subtitle(entry, entry.text, translated)
            })
        else:
            result["output_files"].append({
                "file": f"{input_file}_{target_lang}.{output_format}",
                "preview": translated[:50]
            })
    
    return result

def generate_subtitle_file(
    text: str,
    target_lang: str = "en",
    output_format: str = "srt",
    style: str = "classic"
) -> dict:
    """
    直接翻译文本生成字幕文件
    
    Args:
        text: 要翻译的文本
        target_lang: 目标语言
        output_format: 输出格式
        style: 字幕样式
    """
    # 将文本拆分成句子
    sentences = [s.strip() for s in re.split(r'[。！？\n]', text) if s.strip()]
    
    entries = []
    current_time = 0
    
    for i, sentence in enumerate(sentences):
        duration = max(2, len(sentence) // 2)  # 估算时长
        start = f"00:{current_time//60:02d}:{current_time%60:02d},000"
        end = f"00:{(current_time+duration)//60:02d}:{(current_time+duration)%60:02d},000"
        
        translated = translate_text(sentence, target_lang)
        entries.append(SubtitleEntry(i+1, start, end, translated))
        current_time += duration
    
    # 输出内容
    output_content = ""
    for entry in entries:
        if output_format == "srt":
            output_content += entry.to_srt() + "\n"
        elif output_format == "ass":
            output_content += entry.to_ass() + "\n"
        elif output_format == "vtt":
            output_content = "WEBVTT\n\n" + entry.to_vtt()
        else:
            output_content += entry.text + "\n"
    
    return {
        "target_lang": target_lang,
        "lang_name": LANGUAGES.get(target_lang, target_lang),
        "entry_count": len(entries),
        "format": output_format,
        "style": style,
        "generated_at": datetime.now().isoformat(),
        "content": output_content,
        "preview": entries[:3]
    }

def format_translate_report(result: dict) -> str:
    """格式化翻译报告"""
    lines = []
    lines.append("🌐 多语言字幕翻译报告")
    lines.append("═" * 50)
    lines.append(f"📅 生成时间：{result['generated_at'][:19]}")
    lines.append(f"📁 输入文件：{result['input_file']}")
    lines.append(f"🌍 源语言：{result['source_lang']}")
    lines.append(f"🎯 目标语言：{result['target_lang']}")
    lines.append(f"📋 输出格式：{result['output_format'].upper()}")
    lines.append(f"📝 双语字幕：{'是' if result['dual'] else '否'}")
    lines.append(f"🎨 字幕样式：{result['style']}")
    lines.append("")
    
    lines.append("【翻译预览】")
    lines.append("─" * 50)
    for entry in result["entries"][:5]:
        lines.append(f"⏱ {entry['time_range']}")
        lines.append(f"  原文：{entry['source']}")
        lines.append(f"  译文：{entry['target']}")
        lines.append("")
    
    lines.append("【输出文件】")
    for i, f in enumerate(result["output_files"][:3], 1):
        lines.append(f"  ✅ {i}. {f['file']}")
    
    lines.append("")
    lines.append("💡 使用说明：")
    lines.append("1. 下载生成的字幕文件")
    lines.append("2. 导入剪映/Pr等剪辑软件")
    lines.append("3. 匹配时间轴使用")
    
    return "\n".join(lines)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="多语言字幕翻译器")
    parser.add_argument("--file", "-f", help="字幕文件路径")
    parser.add_argument("--text", "-t", help="直接翻译文本")
    parser.add_argument("--source", "-s", default="auto", help="源语言")
    parser.add_argument("--target", "-g", default="en", help="目标语言")
    parser.add_argument("--format", "-o", choices=SUBTITLE_FORMATS, default="srt", help="输出格式")
    parser.add_argument("--dual", "-d", action="store_true", help="生成双语字幕")
    parser.add_argument("--style", choices=list(SUBTITLE_STYLES.keys()), default="classic", help="字幕样式")
    parser.add_argument("--list-langs", "-l", action="store_true", help="列出支持的语言")
    parser.add_argument("--format-report", choices=["json", "text"], default="text", help="输出格式")
    
    args = parser.parse_args()
    
    if args.list_langs:
        print("🌍 支持的语言：")
        for code, name in LANGUAGES.items():
            print(f"  {code}: {name}")
    elif args.text:
        result = generate_subtitle_file(
            text=args.text,
            target_lang=args.target,
            output_format=args.format,
            style=args.style
        )
        print(result["content"])
    elif args.file:
        result = translate_subtitle_file(
            input_file=args.file,
            source_lang=args.source,
            target_lang=args.target,
            output_format=args.format,
            dual=args.dual,
            style=args.style
        )
        if args.format_report == "json":
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            print(format_translate_report(result))
    else:
        print("请提供字幕文件（--file）或文本（--text）")
        print("使用 --list-langs 查看支持的语言")
