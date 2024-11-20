# Passport Photo API by IdPhoto.AI  

The **[Passport Photo API](https://idphoto.ai)** from [IdPhoto.AI](https://idphoto.ai) is an all-in-one solution for generating ID photos with a single API call. It simplifies the process of creating passport, visa, and ID photos by handling background removal, cropping, resizing, and specification adjustments automatically.  

---

## Features  

- **End-to-End ID Photo Creation**  
  - Remove background from the original photo.  
  - Crop the image to fit ID/passport/visa requirements.  
  - Adjust the photo size to meet the required specifications.  
  - All these steps are executed seamlessly with a single API call.  

- **Global Specifications Support**  
  - Built-in configurations for various countries.  
  - Easily test with preset specifications like `"australia-passport"`.  

- **Photo Quality Check**  
  - Automatically detect and report issues with the provided photo.  

---

## API Documentation  

### Endpoint  
`POST /v2/makeIdPhoto`  

### Request Body  

```json
{
  "apiKey": "string",
  "apiSecret": "string",
  "imageBase64": "string", // Base64-encoded image data
  "specCode": "string"     // Photo specification code (e.g., "australia-passport")
}
```

### Response Body  
```json
{
  "photoUuid": "string",        // Unique ID of the created ID photo
  "waterMark": boolean,         // Whether the photo contains watermarks
  "idPhotoUrl": "string",       // URL of the generated ID photo
  "originalPhotoUrl": "string", // URL of the original uploaded photo
  "issues": ["string"]          // List of detected issues (see Issue Code section)
}
```

## Supported Specifications  

The API supports specifications for various countries and document types, including:  
- Passports  
- Visas  
- National ID cards  

For a full list of supported `specCode` values, please refer to the **Specifications Guide** in the API documentation.  

---

## Photo Quality Issues  

The `issues` field in the response provides a list of detected problems with the photo. Common issues include:  
- **Background Issues**: Background too light or too dark.  
- **Face Positioning**: Face not centered or not meeting alignment rules.  

---

## Getting Started  

1. **Obtain API Credentials**  
   - Sign up at [IdPhoto.AI](https://idphoto.ai) and get your `apiKey` and `apiSecret`.  

2. **Integrate API**  
   - Use the `/v2/makeIdPhoto` endpoint in your application.  

3. **Test and Deploy**  
   - Test with provided specifications like `"australia-passport"`.  


## Contact
For support or inquiries, contact us at support@idphoto.ai.

IdPhoto.AI - Revolutionizing ID photo generation.
