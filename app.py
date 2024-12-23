import streamlit as st
import cv2
import numpy as np
from repeating_pattern_extractor_single_scale_image import (
    find_repeating_pattern_with_left_to_right_sliding,
    find_repeating_pattern_with_top_to_bottom_sliding
)

# Function to extract repeating pattern unit
def find_repeating_pattern_unit(image, original_image):
    y_min, y_max = find_repeating_pattern_with_top_to_bottom_sliding(image)
    x_min, x_max = find_repeating_pattern_with_left_to_right_sliding(image)
    if all([x_min, x_max, y_min, y_max]):
        if len(original_image.shape) == 2:
            pattern = original_image[y_min:y_max, x_min:x_max]
        else:
            pattern = original_image[y_min:y_max, x_min:x_max, :]
        return pattern
    else:
        return None

# Function to convert image to grayscale
def convert_three_scale_image_to_single_scale_image(image):
    if len(image.shape) == 2:
        return image  # Already grayscale
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Streamlit App Title
st.title("Repeating Pattern Unit Extractor")

# Sidebar Options
st.sidebar.title("Options")
uploaded_file = st.sidebar.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"], key="file_uploader")
reset_button = st.sidebar.button("Reset", key="reset_button")
example_button = st.sidebar.button("Use Example Image", key="example_button")

# Reset functionality
if reset_button:
    st.session_state.clear()
    st.experimental_rerun()

# Use example image functionality
if example_button:
    st.session_state["example_image"] = "images_pattern/rp3.jpg"  # Replace with the path to your example image
    st.session_state["uploaded_file"] = None
    st.session_state["output_image"] = None

# Handle uploaded or example image
if uploaded_file is not None:
    st.session_state["uploaded_file"] = uploaded_file
if "example_image" in st.session_state:
    image_path = st.session_state["example_image"]
    input_image = cv2.imread(image_path)
else:
    if "uploaded_file" in st.session_state and st.session_state["uploaded_file"]:
        file_bytes = np.asarray(bytearray(st.session_state["uploaded_file"].read()), dtype=np.uint8)
        input_image = cv2.imdecode(file_bytes, 1)
    else:
        input_image = None

# Layout: Columns for Input and Output
col1, col2 = st.columns(2)

# Input image display and submission
data_ready = False
with col1:
    if input_image is not None:
        # Resize the image for faster processing if large
        if input_image.shape[0] >= 1000 or input_image.shape[1] >= 1000:
            input_image = cv2.resize(input_image, (input_image.shape[1] // 2, input_image.shape[0] // 2))

        # Validate image dimensions
        if input_image.shape[0] < 100 or input_image.shape[1] < 100:
            st.error("Please upload an image with a resolution of at least 100x100 pixels.")
        else:
            # Display the input image
            st.subheader("Input Image:")
            st.image(input_image, channels="BGR", caption="Repeating Pattern Image", use_column_width=True)

            # Submit button
            if st.button("Submit", key="submit_button"):
                st.session_state["process_button"] = True
                gray_image = convert_three_scale_image_to_single_scale_image(input_image)
                st.session_state["input_image"] = gray_image
                st.session_state["original_image"] = input_image
                data_ready = True

# Output image display and processing
if st.session_state.get("process_button") and data_ready:
    with col2:
        st.subheader("Output Image:")
        with st.spinner("Processing..."):
            output_image = find_repeating_pattern_unit(
                st.session_state["input_image"], st.session_state["original_image"]
            )
            st.session_state["output_image"] = output_image

        # Display the output image or error message
        if output_image is not None:
            st.image(output_image, channels="BGR", caption="Extracted Pattern Image")
            # Add download button
            # is_success, buffer = cv2.imencode(".jpg", output_image)
            # output_bytes = buffer.tobytes()
            # st.download_button(
            #     label="Download Extracted Pattern",
            #     data=output_bytes,
            #     file_name="extracted_pattern.jpg",
            #     mime="image/jpeg",
            # )
        else:
            st.error("No repeating pattern was detected!")

# Help Section
with st.expander("Help"):
    st.write(
        """
        **Instructions:**
        - Upload an image with a clear repeating pattern (e.g., textiles, wallpapers).
        - Supported formats: PNG, JPG, JPEG.
        - Ensure the image resolution is at least 100x100 pixels for accurate results.
        - If no pattern is detected, try another image with clearer repetitions.

        **Features:**
        - Extracts the smallest repeating unit of a pattern from the uploaded image.
        - Use an example image to test the functionality.
        - Reset to clear the current session and start over.
        """
    )


# ------------------------------------------------------------------------------------

# import streamlit as st
# import cv2
# import numpy as np
# from repeating_pattern_extractor_single_scale_image import find_repeating_pattern_with_left_to_right_sliding, find_repeating_pattern_with_top_to_bottom_sliding

# # Function to extract repeating pattern unit
# def find_repeating_pattern_unit(image, original_image):
#     y_min, y_max = find_repeating_pattern_with_top_to_bottom_sliding(image)
#     x_min, x_max = find_repeating_pattern_with_left_to_right_sliding(image)
#     if all([x_min, x_max, y_min, y_max]):
#         if len(original_image.shape) == 2:
#             pattern = original_image[y_min:y_max, x_min:x_max]
#         else:
#             pattern = original_image[y_min:y_max, x_min:x_max, :]
#         return pattern
#     else:
#         return None
    
# def convert_three_scale_image_to_single_scale_image(image):
#     if len(image.shape) == 2:
#         gray_image = image
#     else:
#         gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     return gray_image
    

# # Streamlit App Title
# st.title("Repeating Pattern Unit Extractor")

# # Sidebar Options
# st.sidebar.title("Options")
# uploaded_file = st.sidebar.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])
# reset_button = st.sidebar.button("Reset")
# example_button = st.sidebar.button("Use Example Image")

# # Reset functionality
# if reset_button:
#     st.session_state["uploaded_file"] = None
#     st.session_state["example_image"] = None
#     st.session_state["process_button"] = False
#     st.experimental_rerun()

# # Use example image
# if example_button:
#     st.session_state["example_image"] = "images_pattern/rp3.jpg"  # Replace with the path to your example image

# # Check which image to use
# if "uploaded_file" not in st.session_state:
#     st.session_state["uploaded_file"] = uploaded_file

# if st.session_state.get("example_image"):
#     uploaded_file = st.session_state["example_image"]

# # Layout: Columns for Input and Output
# col1, col2 = st.columns(2)

# with col1:
#     if uploaded_file is not None:
#         try:
#             # Load the image
#             if isinstance(uploaded_file, str):  # Example image
#                 input_image = cv2.imread(uploaded_file)
#             else:
#                 file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
#                 input_image = cv2.imdecode(file_bytes, 1)

#             gray_image = convert_three_scale_image_to_single_scale_image(input_image)
#             # Resize the image for faster processing
#             if input_image.shape[0] >= 1000 or input_image.shape[1] >= 1000:
#                 input_image = cv2.resize(input_image, (input_image.shape[1] // 2, input_image.shape[0] // 2))

#             # Validate image dimensions
#             if input_image.shape[0] < 100 or input_image.shape[1] < 100:
#                 st.error("Please upload an image with a resolution of at least 100x100 pixels.")
#             else:
#                 # Display the input image
#                 st.subheader("Input Image:")
#                 st.image(input_image, channels="BGR", caption="Repeating Pattern Image", use_column_width=True)

#                 # Submit button
#                 if "process_button" not in st.session_state:
#                     st.session_state["process_button"] = False

#                 if st.button("Submit"):
#                     st.session_state["process_button"] = True
#                     st.session_state["input_image"] = gray_image
#         except Exception as e:
#             st.error(f"Error processing the uploaded image: {str(e)}")

# if st.session_state.get("process_button") and st.session_state.get("input_image") is not None:
#     with col2:
#         st.subheader("Output Image:")
#         output_placeholder = st.empty()

#         # Show spinner while processing
#         with st.spinner("Processing..."):
#             output_image = find_repeating_pattern_unit(st.session_state["input_image"], input_image)


#         # Display the output image or error message
#         if output_image is not None:
#             output_placeholder.image(output_image, channels="BGR", caption="Extracted Pattern Image")

#             # # Add download button
#             # is_success, buffer = cv2.imencode(".jpg", output_image)
#             # output_bytes = buffer.tobytes()
#             # st.download_button(
#             #     label="Download Extracted Pattern",
#             #     data=output_bytes,
#             #     file_name="extracted_pattern.jpg",
#             #     mime="image/jpeg",
#             # )
#         else:
#             st.error("No repeating pattern was detected!")

# # Help Section
# with st.expander("Help"):
#     st.write(
#         """
#         **Instructions:**
#         - Upload an image with a clear repeating pattern (e.g., textiles, wallpapers).
#         - Supported formats: PNG, JPG, JPEG.
#         - Ensure the image resolution is at least 100x100 pixels for accurate results.
#         - If no pattern is detected, try another image with clearer repetitions.

#         **Features:**
#         - Extracts the smallest repeating unit of a pattern from the uploaded image.
#         - Use an example image to test the functionality.
#         """
#     )




# import streamlit as st
# import cv2
# import numpy as np
# from RpeFinal import find_repeating_pattern_with_left_to_right_sliding, find_repeating_pattern_with_top_to_bottom_sliding


# def find_repeating_pattern_unit(image):
#     y_min, y_max = find_repeating_pattern_with_top_to_bottom_sliding(image)
#     x_min, x_max = find_repeating_pattern_with_left_to_right_sliding(image)
#     if all([x_min, x_max, y_min, y_max]):
#         pattern = image[y_min:y_max, x_min:x_max, :]
#         return pattern
#     else:
#         return None

# # Title
# st.title("Repeating Pattern Unit Extractor")

# # Sidebar for Upload and Reset options
# st.sidebar.title("Options")
# uploaded_file = st.sidebar.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])
# reset_button = st.sidebar.button("Reset")
# example_button = st.sidebar.button("Use Example Image")

# # Reset functionality
# if reset_button:
#     st.experimental_rerun()

# # Use example image
# if example_button:
#     uploaded_file = "images_pattern\\rp3.jpg" # Replace with the path to an example image

# # Layout: Columns for Input and Output
# col1, col2 = st.columns(2)

# with col1:
#     if uploaded_file is not None:
#         try:
#             # Load the image
#             if isinstance(uploaded_file, str):  # Example image
#                 input_image = cv2.imread(uploaded_file)
#                 print(input_image.shape)

#             else:
#                 file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
#                 input_image = cv2.imdecode(file_bytes, 1)
            
#             # Resize the image for faster processing 
#             if input_image.shape[0] >= 1000 or input_image.shape[1] >= 1000:
#                 input_image = cv2.resize(input_image, (input_image.shape[1]//2, input_image.shape[0]//2))
            
#             # Validate image dimensions
#             if input_image.shape[0] < 100 or input_image.shape[1] < 100:
#                 st.error("Please upload an image with a resolution of at least 100x100 pixels.")
#             else:
#                 # Display the input image
#                 st.subheader("Input Image:")
#                 st.image(input_image, channels="BGR", caption="Repeating Pattern Image", use_column_width=True)

#                 # Submit button
#                 process_button = st.button("Submit")
#         except Exception as e:
#             st.error(f"Error processing the uploaded image: {str(e)}")

# if uploaded_file is not None and process_button:
#     with col2:
#         st.subheader("Output Image:")
#         output_placeholder = st.empty()

#         # Show spinner while processing
#         with st.spinner("Processing..."):
#             output_image = find_repeating_pattern_unit(input_image)

#         # Display the output image or error message
#         if output_image is not None:
#             output_placeholder.image(output_image, channels="BGR", caption="Extracted Pattern Image")

#             # # Add download button
#             # is_success, buffer = cv2.imencode(".jpg", output_image)
#             # output_bytes = buffer.tobytes()
#             # st.download_button(
#             #     label="Download Extracted Pattern",
#             #     data=output_bytes,
#             #     file_name="extracted_pattern.jpg",
#             #     mime="image/jpeg",
#             # )
#         else:
#             st.error("No repeating pattern was detected!")

# # Help Section
# with st.expander("Help"):
#     st.write(
#         """
#         **Instructions:**
#         - Upload an image with a clear repeating pattern (e.g., textiles, wallpapers).
#         - Supported formats: PNG, JPG, JPEG.
#         - Ensure the image resolution is at least 100x100 pixels for accurate results.
#         - If no pattern is detected, try another image with clearer repetitions.

#         **Features:**
#         - Extracts the smallest repeating unit of a pattern from the uploaded image.
#         - Use an example image to test the functionality.
#         """
#     )

# ------------------------------------------------------------------------------------------------------------------



# - Download the extracted pattern as a new image.

