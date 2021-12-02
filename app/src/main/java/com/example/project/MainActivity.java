package com.example.project;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {
    private Button login_btn;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        login_btn=findViewById(R.id.login_btn);
        login_btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent= new Intent(MainActivity.this,login.class);
                startActivity(intent);
            }
        });
        Intent intent=getIntent();
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        Intent intent=getIntent();
        intent.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
    }
}