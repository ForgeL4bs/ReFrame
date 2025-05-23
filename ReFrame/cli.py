import argparse
import os
from ReFrame.extract_frames import extract_frames
from ReFrame.image_converter import convert_image
from ReFrame.gif_creator import create_gif
from ReFrame.image_resizer import resize_image_files
from ReFrame.background_remover import remove_background, process_directory

def main():
    parser = argparse.ArgumentParser(
        description=(
            "ReFrame-CLI: ImageToolKit\n"
            "Now supports frame extraction, image conversion, GIF creation, image resizing and background removal.\n\n"
            "Examples:\n"
            "  Extract frames: reframe extractf -input video.mp4 -output ./frames -fps 1\n"
            "  Convert images: reframe convert -input ./images -output ./converted -f png\n"
            "  Create GIF: reframe gifc -input ./images -output ./output.gif -d 100\n"
            "  Resize images: reframe resize -input ./images -output ./resized -wh 800 -ht 600\n"
            "  Remove background: reframe bgremove -input ./images -output ./bg_removed -color 255,255,255\n"
        ),
        formatter_class=argparse.RawTextHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    #subcommand: extract
    extract_parser = subparsers.add_parser("extractf", help="Extract frames from a video")
    extract_parser.add_argument("-input", "--input_path", required=True, help="Path to the video file")
    extract_parser.add_argument("-output", "--output_dir", required=True, help="Directory to save the extracted frames")
    extract_parser.add_argument("-f", "--format", default="png", choices=["png", "jpg", "jpeg"],
                                help="Format of the output frames (png or jpg). Default is png.")
    extract_parser.add_argument("-fps", "--fps", type=float,
                                help="Frames per second to extract. If not specified, extracts all frames.")
    extract_parser.add_argument("-start", "--start_time", type=float,
                                help="Start time (in seconds) for frame extraction.")
    extract_parser.add_argument("-end", "--end_time", type=float,
                                help="End time (in seconds) for frame extraction.")

    #subcommand: convert
    convert_parser = subparsers.add_parser("convert", help="Convert images to different formats(e.g., png, jpg, jpeg, heif, etc.)")
    convert_parser.add_argument("-input", "--input_path", required=True, help="Path to the image file or directory")
    convert_parser.add_argument("-output", "--output_dir", required=True, help="Directory to save the converted images")
    convert_parser.add_argument("-f", "--format", required=True, choices=["png", "jpg", "jpeg", "webp", "heic", "heif"],
                                help="The desired output format")

    #subcommand: gif
    gif_parser = subparsers.add_parser("gifc", help="Create an animated GIF by stakcing up images")
    gif_parser.add_argument("-input", "--input_path", required=True, help="Path to the directory containing images")
    gif_parser.add_argument("-output", "--output_dir", required=True, help="Path to save the output GIF file must be specified with .gif format")
    gif_parser.add_argument("-d", "--duration", type=int, default=100,
                             help="Duration of each frame in the GIF in milliseconds (default: 100ms)")
    
    #subcommand: resize
    resize_parser = subparsers.add_parser("resize", help="Resize images with focal point control")
    resize_parser.add_argument("-input", "--input_path", required=True, help="Path to the image file or directory")
    resize_parser.add_argument("-output", "--output_dir", required=True, help="Directory to save the resized images")
    resize_parser.add_argument("-wh", "--width", type=int, help="The width to which you need to resize the original image")
    resize_parser.add_argument("-ht", "--height", type=int, help="The height to which you need to resize the original image")
    resize_parser.add_argument("-ratio", "--ratio", type=str, help="The desired aspect ratio (e.g., '1:1', '1:2', '3:4')")
    resize_parser.add_argument("-fp", "--focal_point", type=str, default="auto",
                            help="The focal point for resizing (left, right, top, bottom, center, auto, default: auto)")
    resize_parser.add_argument("-f", "--format", type=str, choices=["png", "jpg", "jpeg"], help="The desired output format (png, jpg, jpeg)")
    resize_parser.add_argument("-multi", "--multiplier", type=float, help="The resizing multiplier (e.g., 2 for 2x)")

    #subcommand: bgremove
    bgremove_parser = subparsers.add_parser(
    "bgremove",
    help="Remove the background from images and optionally replace it with a specified color")
    bgremove_parser.add_argument("-input", "--input_path", required=True, help="Path to the image file or directory")
    bgremove_parser.add_argument("-output", "--output_dir", required=True, help="Directory to save the processed images")
    bgremove_parser.add_argument("-color", "--background_color", type=str,
                                help="Background color to replace the transparent background (e.g., '255,255,255' for white).")
    #parse the arguments
    args = parser.parse_args()

    #routing
    if args.command == "extractf":
        extract_frames(
            video_path=args.input_path,
            output_dir=args.output_dir,
            format=args.format,
            fps=args.fps,
            start_time=args.start_time,
            end_time=args.end_time,
        )
    elif args.command == "convert":
        convert_image(
            image_path=args.input_path,
            output_dir=args.output_dir,
            output_format=args.format,
        )
    elif args.command == "gifc":
        create_gif(
            image_dir=args.input_path,
            output_dir=args.output_dir,
            duration=args.duration,
        )
    elif args.command == "resize":
        resize_image_files(
            image_path=args.input_path,
            output_dir=args.output_dir,
            width=args.width,
            height=args.height,
            ratio=args.ratio,
            focal_point=args.focal_point,
            output_format=args.format,
            multiplier=args.multiplier,
    )
    elif args.command == "bgremove":
        #parse the background color
        background_color = None
        if args.background_color:
            try:
                background_color = tuple(map(int, args.background_color.split(',')))
                if len(background_color) != 3 or not all(0 <= c <= 255 for c in background_color):
                    raise ValueError
            except ValueError:
                print("Error: Invalid background color. Please specify as 'R,G,B' (e.g., '255,255,255' for white).")
                return

        #check if input is a file or directory
        if os.path.isdir(args.input_path):
            process_directory(args.input_path, args.output_dir, background_color)
        elif os.path.isfile(args.input_path):
            output_file = os.path.join(args.output_dir, os.path.basename(args.input_path))
            remove_background(args.input_path, output_file, background_color)
        else:
            print(f"Error: Invalid input path {args.input_path}. Must be a file or directory.")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()